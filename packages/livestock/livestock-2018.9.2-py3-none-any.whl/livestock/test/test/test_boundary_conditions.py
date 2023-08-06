import lib_cmf as lc
import cmf
from matplotlib import pyplot as plt
import numpy as np
import shutil
import xmltodict
import xml.etree.ElementTree as ET


def unpack(folder):
    test_files = folder + '/test_files.zip'
    shutil.unpack_archive(test_files, folder)


def load_results(folder):
    result_file = folder + '/results.xml'

    # Parse file
    result_tree = ET.tostring(ET.parse(result_file).getroot())
    result = xmltodict.parse(result_tree)

    cell_0 = eval(result['result']['cell_0']['surface_water_volume'])
    layer_0 = eval(result['result']['cell_0']['layer_0']['volume'])
    cell_1 = eval(result['result']['cell_1']['surface_water_volume'])
    layer_1 = eval(result['result']['cell_1']['layer_0']['volume'])

    return cell_0, cell_1, layer_0, layer_1

def plot_inlet(folder):
    cell0_vol, cell1_vol, layer0_vol, layer1_vol = load_results(folder)

    x = np.linspace(0, len(cell0_vol), len(cell0_vol))

    plt.figure()
    plt.title('Surface Water Volume')
    plt.plot(x, cell0_vol, label='Cell 0')
    plt.plot(x, cell1_vol, label='Cell 1')
    plt.xlabel('Time in h')
    plt.ylabel('Volume in m3')
    plt.legend()
    plt.show()

    plt.figure()
    plt.title('Soil Layer Volume')
    plt.plot(x, layer0_vol, label='Cell 0 - Layer 0')
    plt.plot(x, layer1_vol, label='Cell 1 - Layer 0')
    plt.xlabel('Time in h')
    plt.ylabel('Volume in m3')
    plt.legend()
    plt.show()


def test_inlet():

    folder_path = '/home/ocni/pycharm/deployed_projects/livestock_cmf/test/cmf_boundary_conditions/inlet'
    unpack(folder_path)

    model = lc.CMFModel(folder_path)
    p = model.run_model()

    #print(cmf.describe(p))

    plot_inlet(folder_path)


test_inlet()