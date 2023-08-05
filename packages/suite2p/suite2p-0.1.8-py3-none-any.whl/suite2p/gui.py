from PyQt5 import QtGui, QtCore
import pyqtgraph as pg
from pyqtgraph import console
import sys
import numpy as np
import os
import pickle
from suite2p import fig
from suite2p import run_s2p

### custom QDialog which allows user to fill in ops and run suite2p!
class RunWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(RunWindow, self).__init__(parent)
        self.setGeometry(50,50,1100,700)
        self.setWindowTitle('Choose run options')
        self.win = QtGui.QWidget(self)
        self.layout = QtGui.QGridLayout()
        #layout = QtGui.QFormLayout()
        self.win.setLayout(self.layout)
        # initial ops values
        self.ops = run_s2p.default_ops()
        self.data_path = []
        self.save_path = []
        self.fast_disk = []
        tifkeys = ['nplanes','nchannels','functional_chan','diameter','tau','fs']
        parkeys = ['num_workers','num_workers_roi']
        regkeys = ['nimg_init', 'batch_size', 'maxregshift', 'align_by_chan', 'reg_tif']
        cellkeys = ['navg_frames_svd','nsvd_for_roi','threshold_scaling']
        neukeys = ['ratio_neuropil_to_cell','inner_neuropil_radius','outer_neuropil_radius','min_neuropil_pixels']
        deconvkeys = ['win_baseline','sig_baseline','prctile_baseline','neucoeff']
        keys = [[],tifkeys, parkeys, regkeys, cellkeys, neukeys, deconvkeys]
        labels = ['Filepaths','Main settings','Parallel','Registration','Cell detection','Neuropil','Deconvolution']
        tooltips = ['each tiff has this many planes in sequence',
                    'each tiff has this many channels per plane',
                    'this channel is used to extract functional ROIs (1-based)',
                    'approximate size of the cells in FOV in pixels',
                    'timescale of sensor in deconvolution (in seconds)',
                    'sampling rate (total across planes)',
                    '0 to select num_cores, -1 to disable parallelism, N to enforce value',
                    '0 to select number of planes, -1 to disable parallelism, N to enforce value',
                    '# of subsampled frames for finding reference image',
                    'number of frames per batch',
                    'max allowed registration shift, as a fraction of frame max(width and height)',
                    'when multi-channel, you can align by non-functional channel (1-based)',
                    'if 1, registered tiffs are saved',
                    'max number of binned frames for the SVD',
                    'max number of SVD components to keep for ROI detection',
                    'adjust the automatically determined threshold by this scalar multiplier',
                    'minimum ratio between neuropil radius and cell radius',
                    'number of pixels between ROI and neuropil donut',
                    'maximum neuropil radius',
                    'minimum number of pixels in the neuropil',
                    'window for maximin',
                    'smoothing constant for gaussian filter',
                    'smoothing constant for gaussian filter',
                    'neuropil coefficient']
        l=0
        self.keylist = []
        self.editlist = []
        kk=0
        for lkey in keys:
            k = 0
            qlabel = QtGui.QLabel(labels[l])
            bigfont = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)
            qlabel.setFont(bigfont)
            self.layout.addWidget(qlabel,0,l,1,1)
            for key in lkey:
                lops = 1
                if self.ops[key] or (self.ops[key] == 0):
                    qedit = QtGui.QLineEdit()
                    qlabel = QtGui.QLabel(key)
                    qlabel.setToolTip(tooltips[kk])
                    if type(self.ops[key]) is not bool:
                        qedit.setText(str(self.ops[key]))
                    else:
                        qedit.setText(str(int(self.ops[key])))
                    self.layout.addWidget(qlabel,k*2+1,l,1,1)
                    self.layout.addWidget(qedit,k*2+2,l,1,1)
                    self.keylist.append(key)
                    self.editlist.append(qedit)
                k+=1
                kk+=1
            l+=1
        # data_path
        btiff = QtGui.QPushButton('Add directory to data_path')
        btiff.clicked.connect(self.get_folders)
        self.layout.addWidget(btiff,0,0,1,1)
        qlabel = QtGui.QLabel('data_path')
        qlabel.setFont(bigfont)
        self.layout.addWidget(qlabel,1,0,1,1)
        # save_path0
        bsave = QtGui.QPushButton('Add save_path (default is data_path)')
        bsave.clicked.connect(self.save_folder)
        self.layout.addWidget(bsave,10,0,1,1)
        self.savelabel = QtGui.QLabel('')
        self.layout.addWidget(self.savelabel,11,0,1,1)
        # fast_disk
        bbin = QtGui.QPushButton('Add fast_disk (default is save_path)')
        bbin.clicked.connect(self.bin_folder)
        self.layout.addWidget(bbin,12,0,1,1)
        self.binlabel = QtGui.QLabel('')
        self.layout.addWidget(self.binlabel,13,0,1,1)
        self.runButton = QtGui.QPushButton('RUN SUITE2P')
        self.runButton.clicked.connect(lambda: self.run_S2P(parent))
        self.layout.addWidget(self.runButton,15,0,1,1)
        self.textEdit = QtGui.QTextEdit()
        self.layout.addWidget(self.textEdit, 16,0,15,l)
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.stdout_write)
        self.process.readyReadStandardError.connect(self.stderr_write)
        # disable the button when running the s2p process
        self.process.started.connect(self.started)
        self.process.finished.connect(lambda: self.finished(parent))
        # stop process
        self.stopButton = QtGui.QPushButton('STOP')
        self.stopButton.setEnabled(False)
        self.layout.addWidget(self.stopButton, 15,1,1,1)
        self.stopButton.clicked.connect(self.stop)

    def stop(self):
        self.finish = False
        self.process.kill()

    def started(self):
        self.runButton.setEnabled(False)
        self.stopButton.setEnabled(True)

    def finished(self, parent):
        self.runButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        if self.finish and not self.error:
            cursor = self.textEdit.textCursor()
            cursor.movePosition(cursor.End)
            cursor.insertText('Opening in GUI (can close this window)\n')
            parent.fname = os.path.join(self.save_path, 'suite2p', 'plane0','stat.npy')
            parent.load_proc()
        elif not self.error:
            cursor = self.textEdit.textCursor()
            cursor.movePosition(cursor.End)
            cursor.insertText('Interrupted by user (not finished)\n')
        else:
            cursor = self.textEdit.textCursor()
            cursor.movePosition(cursor.End)
            cursor.insertText('Interrupted by error (not finished)\n')

    def stdout_write(self):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAllStandardOutput(), 'utf-8'))
        self.textEdit.ensureCursorVisible()

    def stderr_write(self):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText('>>>ERROR<<<\n')
        cursor.insertText(str(self.process.readAllStandardError(), 'utf-8'))
        self.textEdit.ensureCursorVisible()
        self.error = True

    def run_S2P(self, parent):
        self.finish = True
        self.error = False
        k=0
        for key in self.keylist:
            if type(self.ops[key]) is float:
                self.ops[key] = float(self.editlist[k].text())
                #print(key,'\t\t', float(self.editlist[k].text()))
            elif type(self.ops[key]) is int or bool:
                self.ops[key] = int(self.editlist[k].text())
                #print(key,'\t\t', int(self.editlist[k].text()))
            k+=1
        self.db = {}
        self.db['data_path'] = self.data_path
        self.db['subfolders'] = []
        if len(self.save_path)==0:
            fpath = self.db['data_path'][0]
            self.save_path = fpath
        self.db['save_path0'] = self.save_path
        if len(self.fast_disk)==0:
            self.fast_disk = self.save_path
        self.db['fast_disk'] = self.fast_disk
        print('Running suite2p!')
        print('starting process')
        np.save('ops.npy', self.ops)
        np.save('db.npy', self.db)
        self.process.start('python -u -W ignore -m suite2p --ops ops.npy --db db.npy')

    def get_folders(self):
        name = QtGui.QFileDialog.getExistingDirectory(self, "Add directory to data path")
        self.data_path.append(name)
        self.layout.addWidget(QtGui.QLabel(name),
                              len(self.data_path)+1,0,1,1)

    def save_folder(self):
        name = QtGui.QFileDialog.getExistingDirectory(self, "Save folder for data")
        self.save_path = name
        self.savelabel.setText(name)

    def bin_folder(self):
        name = QtGui.QFileDialog.getExistingDirectory(self, "Folder for binary file")
        self.fast_disk = name
        self.binlabel.setText(name)

### custom QDialog which makes a list of items you can include/exclude
class ListChooser(QtGui.QDialog):
    def __init__(self, Text, parent=None):
        super(ListChooser, self).__init__(parent)
        self.setGeometry(300,300,300,320)
        self.setWindowTitle(Text)
        self.win = QtGui.QWidget(self)
        layout = QtGui.QGridLayout()
        self.win.setLayout(layout)
        #self.setCentralWidget(self.win)
        loadcell = QtGui.QPushButton('Load iscell.npy')
        loadcell.resize(200,50)
        loadcell.clicked.connect(self.load_cell)
        layout.addWidget(loadcell,0,0,1,1)
        loadtext = QtGui.QPushButton('Load txt file')
        loadcell.resize(200,50)
        #loadtext.resize(loadtext.minimumSizeHint())
        loadtext.clicked.connect(self.load_text)
        layout.addWidget(loadtext,0,1,1,1)
        layout.addWidget(QtGui.QLabel('(select multiple using ctrl)'),1,0,1,1)
        self.list = QtGui.QListWidget(parent)
        layout.addWidget(self.list,2,0,5,2)
        #self.list.resize(450,250)
        self.list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        done = QtGui.QPushButton('OK')
        done.resize(done.minimumSizeHint())
        done.clicked.connect(lambda: self.exit_list(parent))
        layout.addWidget(done,8,0,1,2)

    def load_cell(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open iscell.npy file',filter='iscell.npy')
        if name:
            try:
                iscell = np.load(name[0])
                badfile = True
                if iscell.shape[0] > 0:
                    if iscell[0,0]==0 or iscell[0,0]==1:
                        badfile = False
                        self.list.addItem(name[0])

                if badfile:
                    QtGui.QMessageBox.information(self, 'iscell.npy should be 0/1')
            except (OSError, RuntimeError, TypeError, NameError):
                QtGui.QMessageBox.information(self, 'iscell.npy should be 0/1')
        else:
            QtGui.QMessageBox.information(self, 'iscell.npy should be 0/1')


    def load_text(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open *.txt file', filter='text file (*.txt)')
        if name:
            try:
                txtfile = open(name[0], 'r')
                files = txtfile.read()
                txtfile.close()
                files = files.splitlines()
                for f in files:
                    self.list.addItem(f)
            except (OSError, RuntimeError, TypeError, NameError):
                QtGui.QMessageBox.information(self, 'not a text file')
                print('not a good list')

    def exit_list(self, parent):
        parent.trainfiles = []
        i=0
        for item in self.list.selectedItems():
            parent.trainfiles.append(item.text())
            i+=1
        if i==0:
            for r in range(self.list.count()):
                parent.trainfiles.append(self.list.item(r).text())
        self.accept()

### custom QPushButton class that plots image when clicked
# requires buttons to put into a QButtonGroup (parent.viewbtns)
# allows only 1 button to pressed at a time
class ViewButton(QtGui.QPushButton):
    def __init__(self, bid, Text, parent=None):
        super(ViewButton,self).__init__(parent)
        self.setText(Text)
        self.setStyleSheet("background-color: gray; Text-align:left")
        self.setCheckable(True)
        self.resize(self.minimumSizeHint())
        self.clicked.connect(lambda: self.press(parent, bid))
        self.show()
    def press(self, parent, bid):
        ischecked  = self.isChecked()
        if ischecked:
            parent.ops_plot[1] = bid
            M = fig.draw_masks(parent)
            fig.plot_masks(parent,M)
            for btns in parent.viewbtns.buttons():
                btns.setStyleSheet("background-color: gray; Text-align:left;")
            self.setStyleSheet("background-color: blue; Text-align:left;")

### Changes colors of ROIs
# button group is exclusive (at least one color is always chosen)
class ColorButton(QtGui.QPushButton):
    def __init__(self, bid, Text, parent=None):
        super(ColorButton,self).__init__(parent)
        self.setText(Text)
        self.setCheckable(True)
        self.resize(self.minimumSizeHint())
        self.clicked.connect(lambda: self.press(parent, bid))
        self.setStyleSheet("background-color: gray;")
        self.show()
    def press(self, parent, bid):
        ischecked  = self.isChecked()
        if ischecked:
            parent.ops_plot[2] = bid
            if bid==6:
                fig.corr_masks(parent)
            M = fig.draw_masks(parent)
            fig.plot_masks(parent,M)
            fig.plot_colorbar(parent,bid)
            for btns in parent.colorbtns.buttons():
                btns.setStyleSheet("background-color: gray;")
            self.setStyleSheet("background-color: blue;")
