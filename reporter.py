"""
Creating automatic reports about sales data
This sale data is a fake, random generated data in R language.
The objective is to create a automatic report from this particular data to amaze Zer081 staff!

@michelarruda
"""

# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import io
import os
import smtplib
from email.message import EmailMessage
from base64 import b64encode
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def config_email(image_name):
    with open(image_name, 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'Relatório Diário'
    msg['From'] = 'michelarrudala@gmail.com'
    msg['To'] = 'michelarrudala@gmail.com'

    text = MIMEText('Opa minha consagrada aqui está o relatório diário das suas vendas')
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(image_name))
    msg.attach(image)
    return msg


def send_email(msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()

    s.login('michelarrudala@gmail.com',
            '86558179')

    s.sendmail(msg['From'],
               msg['To'], msg.as_string())
    s.quit()


def load_data(file_name):
    # Loading the data
    sales = pd.read_csv(file_name, encoding='latin-1', parse_dates=True)
    sales = sales
    print(sales.head())
    return sales


def data_wrangling(sales):
    # Data manipulation
    sales['currentTime'] = pd.to_datetime(sales['currentTime'])
    sales['Hour'] = sales['currentTime'].apply(lambda x: x.hour)
    sales['Day'] = sales['currentTime'].apply(lambda x: x.day)
    sales['Month'] = sales['currentTime'].apply(lambda x: x.month)
    sales['Year'] = sales['currentTime'].apply(lambda x: x.year)
    return sales


def make_plots(sales):
    # Making a bar plot of total price by region
    sales_by_region = sales.groupby(by='Region', as_index=False).sum().sort_values(by='Price')

    bar1, axs1 = plt.subplots(3, 1, figsize=(7, 7))
    sns.barplot(x=sales_by_region['Region'], y=sales_by_region['Price'], ax=axs1[0], color='blue')

    axs1[0].set_ylabel('Total Vendido')
    axs1[0].set_title('Total de vendas por Região')

    # Making a bar plot of total sold by product
    sales_by_product = sales.groupby(by='productID', as_index=False).sum().sort_values(by='Price')
    # bar2, axs2 = plt.subplots(figsize=(7, 7))
    sns.barplot(x=sales_by_product['productID'], y=sales_by_product['Price'], ax=axs1[1], color='blue')
    axs1[1].set_ylabel('Total Vendido')
    axs1[1].set_title('Total de vendas por Produto')

    # Making a line plot of total sold by hour of the day
    sales_by_hour = sales.groupby(by='Hour', as_index=False).sum()
    # line1, axs3 = plt.subplots(figsize=(7, 7))
    sns.lineplot(x=sales_by_hour['Hour'], y=sales_by_hour['Price'], ax=axs1[2], color='blue')

    axs1[2].set_title('Total vendido por hora')
    axs1[2].set_xlabel('Hora')
    axs1[2].set_ylabel('Total Vendido')

    plt.tight_layout()

    image_name = 'bar1.png'
    bar1.savefig(image_name)
    msg = config_email(image_name)
    send_email(msg)


sales = load_data('./data/Vendas.csv')
sales = data_wrangling(sales)
make_plots(sales)

