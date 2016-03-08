# -*- coding: utf-8 -*- 
import opencv
import numpy as np
from enthought.traits.api import HasTraits, Array, Enum, Int, Bool, Float, Range
from enthought.traits.ui.api import View, Item
import scipy.ndimage.measurements as M
class MorphologyDemo(HasTraits):
    structing_element = Array(shape=(3,3),dtype=np.uint8)
    process_type = Enum("dilate", "erode",
                        "MORPH_OPEN", "MORPH_CLOSE", "MORPH_GRADIENT", "MORPH_TOPHAT",
                        "MORPH_BLACKHAT")
    erzhi_method = Enum("ADAPTIVE_THRESH_MEAN_C","ADAPTIVE_THRESH_GAUSSIAN_C")
    yuzhi_type = Enum("THRESH_BINARY","THRESH_BINARY_INV","THRESH_MASK")
    blocksize = Range(5, 51, 11)
    canshu = Range(0, 20, 0)
    iter = Int(1)
    #bool = Bool(False)
    bool_dilate =Bool(False)
    bool_erode = Bool(False)
    bool_open = Bool(False)
    bool_close = Bool(False)
    bool_gradient = Bool(False)
    bool_tophat = Bool(False)
    bool_blackhat = Bool(False)

    view = View(
        Item("erzhi_method", label=u"平均算法"),
        Item("yuzhi_type", label=u"阈值类型"),
        Item("blocksize", label=u"块大小"),
        Item("canshu", label=u"参数"),
        Item("bool", label=u"是否进行形态学运算"),
        Item("structing_element", label=u"结构元素"),
        Item("process_type", label=u"处理类型"),
        Item("iter", label=u"迭代次数"),
        Item("bool_dilate",label=u"膨胀"),
        Item("bool_erode",label=u"腐蚀"),
        Item("bool_open",label=u"开环运算"),
        Item("bool_close",label=u"闭环运算"),
        Item("bool_gradient",label=u"GRADIENT"),
        Item("bool_tophat",label=u"TOPHAT"),
        Item("bool_blackhat",label=u"BLACKHAT"),
        title = u"Morphology Demo控制面板"
    )

    def __init__(self, *args, **kwargs):
        super(MorphologyDemo, self).__init__(*args, **kwargs)
        self.structing_element = np.ones((3,3), dtype=np.uint8)
        img = cv.imread("bag.png")
        cv.imshow("old",img)
        self.img = cv.Mat()
        cv.cvtColor(img, self.img, cv.CV_BGR2GRAY)
        self.on_trait_change(self.redraw,"erzhi_method,yuzhi_type,blocksize,canshu,structing_element,process_type,iter,bool,bool_erode,bool_dilate,bool_open,bool_close,bool_gradient,bool_tophat,bool_blackhat")
        #self.redraw()

    def redraw(self):
        print "redraw"
        img1 = cv.Mat()
        img2 = cv.Mat()
        method = getattr(cv,self.erzhi_method)
        yuzhi_type = getattr(cv,self.yuzhi_type)
        blocksize = self.blocksize/2*2+1
        cv.adaptiveThreshold(self.img, img1, 255, method, yuzhi_type,
                             blocksize, self.canshu)
        element = cv.asMat(self.structing_element, force_single_channel=True)
        array = np.array([[0,1,0],[1,1,1],[0,1,0]],dtype=np.uint8)
        element2 = cv.asMat(array, force_single_channel=True)
        label, n = M.label(img1[:])
        counts, edges = np.histogram(label, bins=n)
        label_list = np.where(counts > 100)[0][1:]
        index = np.zeros(n+1, dtype=np.int)
        index[label_list] = label_list
        label = index[label]
        img1[label==0] = 0
        if self.bool_dilate:
            cv.dilate(img1, img2, element, iterations=self.iter)
            img1 = img2
        if self.bool_erode:
            cv.erode(img1, img2, element, iterations=self.iter)
            img1 = img2
        if self.bool_gradient:
            cv.morphologyEx(img1, img2, cv.MORPH_GRADIENT, element, iterations=self.iter)
            img1 = img2
        if self.bool_blackhat:
            cv.morphologyEx(img1, img2, cv.MORPH_BLACKHAT, element, iterations=self.iter)
            img1 = img2
        if self.bool_tophat:
            cv.morphologyEx(img1, img2, cv.MORPH_TOPHAT, element, iterations=self.iter)
            img1 = img2
        if self.bool_open:
            cv.morphologyEx(img1, img2, cv.MORPH_OPEN, element, iterations=self.iter)
            img1 = img2
        if self.bool_close:
            cv.morphologyEx(img1, img2, cv.MORPH_CLOSE, element, iterations=self.iter)
            img1 = img2
        cv.imshow("Morphology Demo",img1)

demo = MorphologyDemo()
demo.configure_traits() 