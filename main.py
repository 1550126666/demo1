import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image, ImageFont, ImageDraw
import matplotlib.font_manager as fm
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
port_list = [port.device for port in ports]

user_port = st.sidebar.selectbox("选择user串口", port_list)
data_port = st.sidebar.selectbox("选择data串口", port_list)
def init(azimuth_chart, elevation_chart, plot_chart, breathing_value, heartbeat_value):
    # 更新到达角多普勒热图数据和俯仰角多普勒热图数据
    azimuth_data = np.zeros((100, 100))
    elevation_data = np.zeros((100, 100))

    # 更新呼吸频率和心跳频率数据
    breathing_data = np.zeros(100)
    heartbeat_data = np.zeros(100)
    # 设置图像的尺寸和字体
    fig_width = 8
    fig_height = 6
    dpi = 80
    font_path = "C:/Windows/Fonts/simsun.ttc"  # 请根据您的字体文件路径进行修改
    font_size = 12
    font_prop = fm.FontProperties(fname=font_path)
    title_font = {'fontproperties': font_prop, 'fontsize': 12, 'fontweight': 'bold'}
    # 绘制到达角多普勒热图
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)
    img = ax.imshow(azimuth_data, cmap='hot', interpolation='nearest')
    plt.colorbar(img, ax=ax)
    ax.set_title("到达角多普勒热图", **title_font)

    # 将图像保存到内存中
    azimuth_img_bytes = io.BytesIO()
    plt.savefig(azimuth_img_bytes, format='png')
    plt.close(fig)

    # 将保存的图像加载为PIL对象
    azimuth_img = Image.open(azimuth_img_bytes)
    azimuth_img = azimuth_img.resize((fig_width * dpi, fig_height * dpi))

    # 添加中文字体
    draw = ImageDraw.Draw(azimuth_img)
    font = ImageFont.truetype(font_path, font_size)
    draw.text((10, 10), "到达角多普勒热图", font=font, fill='black')

    # 显示到达角多普勒热图
    azimuth_chart.image(azimuth_img)

    # 绘制俯仰角多普勒热图
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)
    img = ax.imshow(elevation_data, cmap='hot', interpolation='nearest')
    plt.colorbar(img, ax=ax)
    ax.set_title("俯仰角多普勒热图", **title_font)

    # 将图像保存到内存中
    elevation_img_bytes = io.BytesIO()
    plt.savefig(elevation_img_bytes, format='png')
    plt.close(fig)

    # 将保存的图像加载为PIL对象
    elevation_img = Image.open(elevation_img_bytes)
    elevation_img = elevation_img.resize((fig_width * dpi, fig_height * dpi))

    # 添加中文字体
    draw = ImageDraw.Draw(elevation_img)
    draw.text((10, 10), "俯仰角多普勒热图", font=font, fill='black')

    # 显示俯仰角多普勒热图
    elevation_chart.image(elevation_img)

    # 绘制生命体征数据折线图
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)
    ax.plot(breathing_data, label="呼吸频率", )
    ax.plot(heartbeat_data, label="心跳频率")
    ax.legend(prop=font_prop, loc='upper right')
    ax.set_title("生命体征数据折线图", **title_font)

    # 将图像保存到内存中
    plot_img_bytes = io.BytesIO()
    plt.savefig(plot_img_bytes, format='png')
    plt.close(fig)

    # 将保存的图像加载为PIL对象
    plot_img = Image.open(plot_img_bytes)
    plot_img = plot_img.resize((fig_width * dpi, fig_height * dpi))

    # 添加中文字体
    draw = ImageDraw.Draw(plot_img)
    draw.text((10, 10), "生命体征数据折线图", font=font, fill='black')

    # 显示生命体征数据折线图
    plot_chart.image(plot_img)

    # 更新呼吸频率和心跳频率数值
    # breathing_value.write("呼吸频率: {:.2f}".format(np.mean(breathing_data)))
    # heartbeat_value.write("心跳频率: {:.2f}".format(np.mean(heartbeat_data)))
    breathing_value.metric("呼吸频率", "{:.2f}".format(np.mean(breathing_data)) + " bpm")
    heartbeat_value.metric("心跳频率", "{:.2f}".format(np.mean(heartbeat_data)) + " bpm")


def update_data(azimuth_chart, elevation_chart, plot_chart, breathing_value, heartbeat_value):
    # 更新到达角多普勒热图数据和俯仰角多普勒热图数据
    azimuth_data = np.random.rand(100, 100)
    elevation_data = np.random.rand(100, 100)

    # 更新呼吸频率和心跳频率数据
    breathing_data = np.random.rand(100)
    heartbeat_data = np.random.rand(100)

    # 设置图像的尺寸和字体
    fig_width = 8
    fig_height = 6
    dpi = 80
    font_path = "C:/Windows/Fonts/simsun.ttc"  # 请根据您的字体文件路径进行修改
    font_size = 12
    font_prop = fm.FontProperties(fname=font_path)
    title_font = {'fontproperties': font_prop, 'fontsize': 12, 'fontweight': 'bold'}
    # 绘制到达角多普勒热图
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)
    img = ax.imshow(azimuth_data, cmap='hot', interpolation='nearest')
    plt.colorbar(img, ax=ax)
    ax.set_title("到达角多普勒热图",**title_font)

    # 将图像保存到内存中
    azimuth_img_bytes = io.BytesIO()
    plt.savefig(azimuth_img_bytes, format='png')
    plt.close(fig)

    # 将保存的图像加载为PIL对象
    azimuth_img = Image.open(azimuth_img_bytes)
    azimuth_img = azimuth_img.resize((fig_width * dpi, fig_height * dpi))

    # 添加中文字体
    draw = ImageDraw.Draw(azimuth_img)
    font = ImageFont.truetype(font_path, font_size)
    draw.text((10, 10), "到达角多普勒热图", font=font, fill='black')

    # 显示到达角多普勒热图
    azimuth_chart.image(azimuth_img)

    # 绘制俯仰角多普勒热图
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)
    img = ax.imshow(elevation_data, cmap='hot', interpolation='nearest')
    plt.colorbar(img, ax=ax)
    ax.set_title("俯仰角多普勒热图",**title_font)

    # 将图像保存到内存中
    elevation_img_bytes = io.BytesIO()
    plt.savefig(elevation_img_bytes, format='png')
    plt.close(fig)

    # 将保存的图像加载为PIL对象
    elevation_img = Image.open(elevation_img_bytes)
    elevation_img = elevation_img.resize((fig_width * dpi, fig_height * dpi))

    # 添加中文字体
    draw = ImageDraw.Draw(elevation_img)
    draw.text((10, 10), "俯仰角多普勒热图", font=font, fill='black')

    # 显示俯仰角多普勒热图
    elevation_chart.image(elevation_img)

    # 绘制生命体征数据折线图
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)
    ax.plot(breathing_data, label="呼吸频率",)
    ax.plot(heartbeat_data, label="心跳频率")
    ax.legend(prop=font_prop,loc='upper right')
    ax.set_title("生命体征数据折线图",**title_font)

    # 将图像保存到内存中
    plot_img_bytes = io.BytesIO()
    plt.savefig(plot_img_bytes, format='png')
    plt.close(fig)

    # 将保存的图像加载为PIL对象
    plot_img = Image.open(plot_img_bytes)
    plot_img = plot_img.resize((fig_width * dpi, fig_height * dpi))

    # 添加中文字体
    draw = ImageDraw.Draw(plot_img)
    draw.text((10, 10), "生命体征数据折线图", font=font, fill='black')

    # 显示生命体征数据折线图
    plot_chart.image(plot_img)

    # 更新呼吸频率和心跳频率数值
    # breathing_value.write("呼吸频率: {:.2f}".format(np.mean(breathing_data)))
    # heartbeat_value.write("心跳频率: {:.2f}".format(np.mean(heartbeat_data)))
    breathing_value.metric("呼吸频率", "{:.2f}".format(np.mean(breathing_data))+" bpm")
    heartbeat_value.metric("心跳频率", "{:.2f}".format(np.mean(heartbeat_data))+" bpm")

def main():
    col1, col2, col3 = st.columns(3)
    with col1:
        azimuth_chart = st.empty()
        breathing_value = st.empty()
    with col2:
        elevation_chart = st.empty()
        heartbeat_value = st.empty()
    with col3:
        plot_chart = st.empty()
    init(azimuth_chart, elevation_chart, plot_chart, breathing_value, heartbeat_value)


    start_button = st.button("开始")
    stop_button = st.button("停止")

    if start_button and not stop_button:
        while True:
            update_data(azimuth_chart, elevation_chart, plot_chart, breathing_value, heartbeat_value)
            st.empty()

            if stop_button:
                break

if __name__ == "__main__":
    main()