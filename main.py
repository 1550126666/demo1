import time

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
with st.spinner('Wait for it...'):
    time.sleep(1)
su = st.success('Done!')
time.sleep(0.6)
su.empty()
st.title("基于毫米波雷达📡的姿态检测🙋‍♂️以及生命体征检测🫀")


def init(azimuth_chart, elevation_chart, plot_chart, breathing_value, heartbeat_value,posture_result):
    # 更新到达角多普勒热图数据和俯仰角多普勒热图数据
    azimuth_data = np.zeros((100, 100))
    elevation_data = np.zeros((100, 100))
    # 加载姿态预测结果
    posture_data = Image.open("./data/1.png")
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

    # 绘制姿态预测骨架图
    posture_result.image(posture_data, caption='姿态预测',use_column_width = True)
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


def update_data(azimuth_chart, elevation_chart, plot_chart, breathing_value, heartbeat_value, posture_result, num):
    # 更新到达角多普勒热图数据和俯仰角多普勒热图数据
    azimuth_data = np.random.rand(100, 100)
    elevation_data = np.random.rand(100, 100)

    # 加载姿态预测结果
    posture_data = Image.open("./data/{}.png".format(num))

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

    # 绘制姿态预测骨架图
    posture_result.image(posture_data, caption='姿态预测', use_column_width=True)
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
def show_pose_knowledge():
    st.markdown("## 错误坐姿的危害")
    st.markdown("错误的坐姿可能导致以下问题：")
    st.markdown("- 脊柱问题，如脊椎变形、疼痛等。")
    st.markdown("- 颈椎问题，如颈椎痛、僵硬等。")
    st.markdown("- 肌肉疲劳和紧张，导致不适和疼痛。")
    st.markdown("- 姿势相关的呼吸问题。")

    st.markdown("## 如何纠正坐姿")
    st.markdown("以下是纠正坐姿的一些建议：")
    st.markdown("- 保持正确的坐姿，背部挺直、肩部放松。")
    st.markdown("- 使用支撑，如靠背和腰垫。")
    st.markdown("- 定期休息和活动，避免长时间静坐。")
    st.markdown("- 可以尝试一些坐姿矫正设备或者使用正确坐姿的应用程序。")

    st.markdown("## 如何放松身体")
    st.markdown("以下是放松身体的一些方法：")
    st.markdown("- 进行伸展和放松运动，如颈部转动、肩部放松等。")
    st.markdown("- 深呼吸和放松呼吸，帮助缓解压力和紧张感。")
    st.markdown("- 均衡饮食和充足的睡眠，有助于身体的恢复和放松。")



def main():
    col1, col2 = st.columns(2)
    with col1:
        st.header("到达角多普勒热图")
        st.text("根据多普勒热图分析当前检测目标的到达角与距离之间的关系")
        azimuth_chart = st.empty()
    with col2:
        st.header("俯仰角多普勒热图")
        st.text("根据多普勒热图分析当前检测目标的俯仰角与距离之间的关系")
        elevation_chart = st.empty()
    st.header("生命体征检测")
    col3, col4 = st.columns(2)
    with col3:
        st.text("展示呼吸频率与心跳频率的折线图")
        plot_chart = st.empty()
    with col4:
        st.text("展示呼吸频率与心跳频率数据变化")
        scol1, scol2 = st.columns(2)
        with scol1:
            breathing_value = st.empty()
        with scol2:
            heartbeat_value = st.empty()
    st.header("姿态预测结果")
    posture_result = st.empty()
    init(azimuth_chart, elevation_chart, plot_chart, breathing_value, heartbeat_value, posture_result)

   # 在适当的地方调用该函数来展示普及知识区域
    show_pose_knowledge()
    col5, col6 = st.sidebar.columns(2)
    start_button = col5.button("开始")
    stop_button = col6.button("停止")
    num = 1
    if start_button and not stop_button:
        while True:
            if num < 24:
                num = num + 1
            elif num == 24:
                num = 1
            update_data(azimuth_chart, elevation_chart, plot_chart, breathing_value, heartbeat_value, posture_result, num)
            st.empty()

            if stop_button:
                break


if __name__ == "__main__":
    main()
