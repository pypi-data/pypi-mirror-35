from distutils.core import setup
setup(
  name = 'ybc_echarts',
  packages = ['ybc_echarts'],
  version = '1.0.1',
  description = 'ybc_echarts generate chart',
  long_description='ybc_echarts generate chart',
  author = 'KingHS',
  author_email = '382771946@qq.com',
  keywords = ['pip3', 'ybc_echarts', 'python3','python','echats'],
  license='MIT',
  install_requires=[
        'pyecharts',
        'echarts-countries-pypkg',
        'echarts-china-provinces-pypkg',
        'echarts-china-cities-pypkg'
    ]
)
