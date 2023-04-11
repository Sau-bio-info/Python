{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyND0amyXRIuErj8rIjcbDYq",
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
        "<a href=\"https://colab.research.google.com/github/Sau-bio-info/Python/blob/main/list_comphrension.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ekUA6-6o0Cxa"
      },
      "outputs": [],
      "source": [
        "cities=[\"Ahemdabad\",\"Gandhinagar\",\"Shimla\",\"Pune\",\"Mumbai\",\"Nashik\",\"Raipur\",\"Indore\",\"Guwahati\",\"Srinagar\",\"Bengaluru\"]\n",
        "\n",
        "cities_a=[x for x in cities if x != \"Pune\"]\n",
        "\n",
        "print(cities_a)\n",
        "\n",
        "new_list=[x for x in range(20) if x <= 13]\n",
        "\n",
        "print(new_list)\n",
        "\n",
        "#Sets the value for entries in newlist\n",
        "\n",
        "cities_lower=[x.lower() for x in cities]\n",
        "\n",
        "print(cities_lower)\n",
        "\n",
        "#cities_sort=[x.() for x in cities]\n",
        "\n",
        "#print(cities_sort)\n",
        "\n",
        "newlist = [x if x != \"Shimla\" else \"Itanagar\" for x in cities]\n",
        "\n",
        "print(newlist)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "h7yo66-f0Llh"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}