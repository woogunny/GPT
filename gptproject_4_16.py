{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNuRsHD4AOOeGxRgxOTHzZ/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/woogunny/GPT/blob/main/gptproject_4_16.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install openai"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5B6C__mJ3ojI",
        "outputId": "ba04416c-e7b9-423e-eb4d-39776d912eb0"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: openai in /usr/local/lib/python3.10/dist-packages (1.16.2)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.10/dist-packages (from openai) (3.7.1)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from openai) (1.7.0)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.10/dist-packages (from openai) (0.27.0)\n",
            "Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from openai) (2.6.4)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from openai) (1.3.1)\n",
            "Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.10/dist-packages (from openai) (4.66.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.7 in /usr/local/lib/python3.10/dist-packages (from openai) (4.10.0)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai) (3.6)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai) (1.2.0)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai) (2024.2.2)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai) (1.0.5)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai) (0.14.0)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->openai) (0.6.0)\n",
            "Requirement already satisfied: pydantic-core==2.16.3 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->openai) (2.16.3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "1ALE55vv4BUV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "os.environ[\"OPENAI_API_KEY\"] = \"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\"\n",
        "\n",
        "import openai # OpenAI 모듈 불러오기\n",
        "\n",
        "# OpenAI API 키 설정\n",
        "#client = OpenAI(api_key='OPENAI_API_KEY\") # 사용자의 API 키로 대체해야 함\n",
        "\n",
        "openai.api_key = os.getenv(\"OPENAI_API_KEY\")"
      ],
      "metadata": {
        "id": "Rz8GQNqM3sjY"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "from openai import OpenAI\n",
        "client = OpenAI(api_key=\"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\")\n",
        "def ask_chatgpt(messages):\n",
        "  response=client.chat.completions.create(\n",
        "      model=\"gpt-3.5-turbo\", messages=messages\n",
        "  )\n",
        "  return response.choices[0].message.content\n"
      ],
      "metadata": {
        "id": "1OSF-Mpf8-p_"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "os.environ[\"OPENAI_API_KEY\"] = \"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\"\n"
      ],
      "metadata": {
        "id": "SEdPBJ7Q83et"
      },
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 45,
      "metadata": {
        "id": "CrgMSqMq2W6Z"
      },
      "outputs": [],
      "source": [
        "# 파일에서 스크립트 읽기\n",
        "with open(\"transcript.txt\", \"r\") as f:\n",
        "  transcript = f.read()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pwd"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "iROu1bZC6Qyx",
        "outputId": "e26e8cce-2dac-4be2-d009-ebf936d31945"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'/content'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 오픈AI의 채팅 완성 엔드포인트 호출, GPT-4 모델 사용\n",
        "response = client.chat.completions.create(\n",
        "    model=\"gpt-4-1106-preview\",\n",
        "    messages=[\n",
        "        {\"role\": \"system\", \"content\": \"너는 친절한 어시스턴트야.\"},\n",
        "        {\"role\": \"user\", \"content\": \"다음 글을 요약해줘\"},\n",
        "        {\"role\": \"assistant\", \"content\": \"Yes.\"},\n",
        "        {\"role\": \"user\", \"content\": transcript}\n",
        "    ],\n",
        ")\n",
        "\n",
        "# 결과 출력\n",
        "print(response.choices[0].message.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0R2T911v34-5",
        "outputId": "2669582c-23a8-4907-906e-91951b0432b0"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "이 글은 컴퓨터가 숫자를 인식하는 네트워크의 구조와 작동 방식을 설명하고 있습니다. 저해상도로 기록된 숫자 '3'이 인식 가능한 이미지로 언급되며, 사람의 시각처리 과정과 비교하면서 신경망과 머신러닝의 중요성을 강조합니다. 신경망이란 무엇이고, 어떻게 작동하는지 수학적인 개념을 통해 설명합니다. 이와 관련된 구조를 가진 신경망이 가중치(weight), bias, 활성화 함수 등을 통해 이미지의 숫자를 인식하도록 하는 과정을 자세히 다룹니다. 신경망의 기본 구조와 기본적으로 필요한 수학적 개념(가중치 합, 시그모이드 함수, 행렬 곱셈 등)에 대해 설명하면서, 이 신경망이 이미지를 보고 적절한 가중치와 bias를 어떻게 학습하는지는 다음 동영상에서 다룰 예정이라고 안내합니다. 또한, 현대 신경망이 시그모이드 함수보다 ReLU 함수를 선호하는 이유에 대해 간단히 언급합니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "reKKj6DG3C_8"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}