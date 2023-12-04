# UX Research Assistant

The **UX Research Assistant** is a Python-based tool designed to assist UX designers in analyzing data from surveys and interviews. It leverages the power of OpenAI's GPT-4 model to help streamline the UX design process by providing insights and assistance in data analysis.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **UX Research Assistant** is specifically tailored to assist UX designers by reading and analyzing data from surveys and interviews. Its primary tasks include creating affinity diagram, categorizing and clustering information based on user pain points, and translating these insights into empathy map. This automation aims to make data analysis more efficient and insightful, allowing designers to focus on creating better user experiences.

## Features

- **Data Analysis:** The bot uses the OpenAI GPT-4 model to analyze data from surveys and interviews.
- **Affinity Diagrams:** It assists in creating affinity diagrams to organize and visualize data.
- **Categorization:** The bot categorizes and clusters information based on identified user pain points.
- **Empathy Maps:** It helps translate categorized insights into empathy maps.
- **Efficiency:** By automating data analysis tasks, it saves time and allows designers to focus on UX design.

## Getting Started

### Installation

Before using the **UX Research Assistant**, you need to set up the required environment:

1. Clone the repository:

   ```bash
   git clone https://github.com/laurapaschoal/ux-research-assistant.git
   ```

2. Install the necessary Python packages:

   ```bash
   pip install langwatch openai chainlit
   ```

3. Create an OpenAI API key and export it with `export OPENAI_API_KEY=<your key>` before running the bot.

### Usage

To use the bot, follow these steps:

1. Initialize the bot by running the Python script with `chainlit run main.py -w`

2. Provide research interviews and surveys, and the bot will respond with analysis and insights based on the provided data.

3. The bot will help you create affinity diagrams, categorize information, and generate empathy maps.

## Contributing

Contributions to the **UX Research Assistant** project are welcome. If you have ideas for improvements or would like to report issues, please open a GitHub issue or submit a pull request.
