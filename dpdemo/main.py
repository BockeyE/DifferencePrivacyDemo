import math
import time

from dpdemo.filesystem import FileSystem


class ioparameters(object):
    def __init__(self):
        self.n = 0  # number vertices in input graph
        self.m = 0  # number of edges in input graph
        self.d_dir = ''  # working directory
        self.f_in = ''  # name of input file (either .pairs or .hrg)
        self.flag_f = True  # name of output hrg file
        self.f_dg = ''  # name of output hrg file
        self.f_dg_info = ''  # name of output information-on-hrg file
        self.dg_scratch = ''
        self.f_stat = ''  # name of output statistics file
        self.f_pairs = ''  # name of output random graph file
        self.f_namesLUT = ''  # name of output names LUT file
        self.flag_make = True  # flag for if -make invoked
        self.s_scratch = ''  # filename sans extension
        self.s_tag = ''  # user defined filename tag
        self.start_time = ''  # time simulation was started
        self.timer = 0  # timer for reading input
        self.flag_timer = True  # flag for when timer fires
        self.flag_compact = True  # compact the Lxy file
        self.out_dir = ''  # output directory
        self.epsilon_hrg = 0  # noise scale for hrg
        self.epsilon_edge = 0  # noise scale for edge
        self.T = 0  # constant for differential privacy
        self.thresh_eq = 0  # threshold for manually forcing MCMC stop after thresh_eq*ioparm.n steps and reaching convergence
        self.thresh_stop = 0  # threshold for manually stop MCMC stop after thresh_stop*ioparm.n


def recordNamesLUT():
    return
    # reverseNamesLUT = rbtree()
    # head = []  # keyValuePair
    # prev = []
    # head = namesLUT.returnTreeAsList()
    # while head:
    #     reverseNamesLUT.insertItem(head.y, head.x)
    #     prev = head
    #     head = head.next
    # head = None
    # prev = None
    #
    # elementrb = []
    # ofstream
    # fout(ioparm.f_namesLUT.c_str(), ios::trunc)
    # fout << "virtual\treal\n"
    # for i in range(0, ioparm.n):
    #     item = reverseNamesLUT.findItem(i)
    #     fout << i << "\t" << item.value << "\n"
    # fout.close()
    # return


def readNamesLUT():
    n, s, f = 0
    headline = ''

    # ofstream是从内存到硬盘,ifstream是从硬盘到内存
    # ifstream
    # c_str()函数返回一个指向正规C字符串的指针, 内容与本string串相同.
    # ios::in 读 文件不存在 就无法打开
    # fscan1(ioparm.f_namesLUT.c_str(), ios:: in )

    # getline()函数是一个比较常见的函数。根据名字直接"望文->生义"，就知道这个函数是来完成读入一行数据。
    # getline(fscan1, headline)

    # ifstream ifs(filename.c_str()) // 用文件输入流读入文件名为filename这个文件
    # string s // 定义string类对象
    # while( ifs >> s) // 循环在文件输入流中读入一个字符串
    # cout << s << "\n" // 读入一个，打印一个，并打印换行

    with open(ioparm.f_namesLUT, "r") as f:
        headline = f.readline()
        print(headline)

    # namesLUT is  a  rbtree
    # while fscan1 >> s >> f:
    #     if namesLUT.findItem(s) is None:
    #         namesLUT.insertItem(s, f)
    #         n = n + 1
    #         ioparm.n = n
    return


def readPairsFile():
    return


def MCMCEquilibrium_Find(t):
    return


def num2str(inputs):
    return


def parseCommandLine(argc, argv):
    return


def readPairsFile():
    return


def recordHRG(step, count, thisL):
    return


def recordHRGSample(thisL, sample_num, step):
    return


def MCMCEquilibrium_Sample(num_samples, T, flag_control=True):
    return


def recordLogL(trace, len):
    return


def check_convergence(check_trace, len):
    return


def recordRandomGraphStructure(out_file, random_g):
    return


def recordRandomGraphInfo(outfilem, thisL, m):
    return


if __name__ == '__main__':
    ioparm = ioparameters()
    namesLUT = rbtree()
    d = dendro()
    t = 0
    bestL = float(0)
    out_count = 0
    period = 10000
    Likeli = []

    ioparm.n = 0
    ioparm.timer = 20
    ioparm.s_tag = ""
    # time_t实际上是长整型
    t1 = time.time()
    num_samples = 10
    flag_control = True

    d = dendro()
    ioparm.start_time = time.time()
    # if (parseCommandLine(argc, argv)) :
    if ioparm.flag_f:
        # //1. read .pairs file,
        # //2. run MCMC until equilbrium
        # //3. sample HRG and generate random graph

        # // read input .pairs file
        readPairsFile()

        if ioparm.epsilon_hrg:
            # 使用floor函数。floor(x)返回的是小于或等于x的最大整数。
            # 使用ceil函数。ceil(x)返回的是大于x的最小整数。

            N = math.ceil(ioparm.n / 2.0) * math.floor(ioparm.n / 2.0)
            p = 1.0 / N
            deltaU = math.fabs(math.log(p) + (N - 1) * math.log(1 - p))
            ioparm.T = ioparm.epsilon_hrg / (2 * deltaU)
            print("epsilon hrg: ", ioparm.epsilon_hrg)
            print("T: ", ioparm.T)
        else:
            ioparm.T = 1.0
            print("T: ", ioparm.T)
        print("sensitivity for hrg: : ", ioparm.T)
        print(">> beginning convergence to equilibrium\n")
        # main函数的返回值
        # main函数的返回值用于说明程序的退出状态。如果返回0，则代表程序正常退出。
        if not (MCMCEquilibrium_Find(ioparm.T)):
            # return 0  # run it to equilibrium ,程序正常结束
            exit()
        print("\n>> convergence critera met\n>> beginning sampling\n")
        if not (MCMCEquilibrium_Sample(num_samples, ioparm.T, flag_control)):
            # return 0  # // sample likelihoods for missing connections
            exit()
        print(">> sampling finished")
    elif ioparm.flag_make:
        readNamesLUT()
        print(">> begin import dendrogram: ", ioparm.f_dg)
        print(">> make random graph with epsilon value: ", ioparm.epsilon_edge)
        if not (d.importDendrogramStructure(ioparm.f_dg)):
            print("Error: Malformed input file.\n")
            exit()

        num_of_graph = 1
        i = 0
        while i < num_of_graph:
            i = i + 1
            randomG = graph(ioparm.n)
            timestamp = ""
            # filesystem::getTimeStamp(timestamp)
            FileSystem.getTimeStamp(timestamp)
            outfile = ioparm.out_dir + ioparm.dg_scratch + "_random_graph_" + timestamp
            thisL = d.getLikelihood()
            d.makeNoisyRandomGraph(randomG, ioparm.epsilon_edge, flag_control)
            recordRandomGraphStructure(outfile + ".pairs", randomG)
            print("number of nodes: ", randomG.numNodes())
            print("number of links: ", randomG.numLinks())
            print("number of simple edges: ", randomG.numLinks() / 2)
            num_of_edges = randomG.numLinks() / 2
            recordRandomGraphInfo(outfile + ".info", thisL, num_of_edges)
