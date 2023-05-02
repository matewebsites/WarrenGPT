import json
import time
import datetime
import pandas as pd
import tweepy
import os
import numpy as np
import openai_secret_manager
import alpaca_trade_api as tradeapi
from transformers import pipeline
from google.cloud import automl_v1beta1 as automl
import azureml.core
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.authentication import ServicePrincipalAuthentication
import nvidia.dali.ops as ops
import nvidia.dali.types as types
import tensorflow as tf
import tensorflow_agents as tf_agents
import gym
import matplotlib.pyplot as plt
import openai

# Set up OpenAI API credentials
openai.api_key = openai_secret_manager.get_secret("openai_api_key")["api_key"]

# Authenticate to Alpaca paper trading API
key_id = openai_secret_manager.get_secret("alpaca_paper_key_id")["api_key"]
secret_key = openai_secret_manager.get_secret("alpaca_paper_secret_key")["api_key"]
base_url = "https://paper-api.alpaca.markets"
api = tradeapi.REST(key_id, secret_key, base_url, api_version='v2')

# Authenticate to Twitter API
consumer_key = openai_secret_manager.get_secret("twitter_consumer_key")["api_key"]
consumer_secret = openai_secret_manager.get_secret("twitter_consumer_secret")["api_key"]
access_token = openai_secret_manager.get_secret("twitter_access_token")["api_key"]
access_token_secret = openai_secret_manager.get_secret("twitter_access_token_secret")["api_key"]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api_twitter = tweepy.API(auth)

# Authenticate to Twelve Data API
td_api_key = openai_secret_manager.get_secret("twelvedata_api_key")["api_key"]

# Authenticate to Yahoo Finance API
yf_api_key = openai_secret_manager.get_secret("yahoo_finance_api_key")["api_key"]

# Authenticate to RealStonks API
rs_api_key = openai_secret_manager.get_secret("realstonks_api_key")["api_key"]

# Authenticate to Alpha Vantage API
av_api_key = openai_secret_manager.get_secret("alpha_vantage_api_key")["api_key"]

# Authenticate to Finage Currency Data Feed API
finage_api_key = openai_secret_manager.get_secret("finage_api_key")["api_key"]

# Authenticate to Bitquery API
bq_api_key = openai_secret_manager.get_secret("bitquery_api_key")["api_key"]

# Authenticate to Coinbase API
cb_api_key = openai_secret_manager.get_secret("coinbase_api_key")["api_key"]
cb_secret_key = openai_secret_manager.get_secret("coinbase_secret_key")["api_key"]
cb_passphrase = openai_secret_manager.get_secret("coinbase_passphrase")["api_key"]
cb_base_url = "https://api.pro.coinbase.com"
cb_auth = {
    "key": cb_api_key,
    "secret": cb_secret_key,
    "passphrase": cb_passphrase
}

# Authenticate to Binance API
bn_api_key = openai_secret_manager.get_secret("binance_api_key")["api_key"]
bn_secret_key = openai_secret_manager.get_secret("binance_secret_key")["api_key"]
bn_base_url = "https://api.binance.com"
bn_auth = {
    "X-MBX-APIKEY": bn_api_key
}

# Function to get current stock price from Alpaca
def get_stock_price(ticker):
