---
categories:
- Tools
date: '2023-10-17'
tags:
- artificial intelligence
title: Generative AI beyond ChatGPT
---

While the advent of ChatGPT has garnered significant attention in the
Technology world, Generative AI extends far beyond this celebrated model. I
recently took the course "Generative AI with Large Language Models" from
DeepLearning.AI and AWS helped me to unravel its core principles and practical
applications that have the potential to reshape the landscape of technology
and innovation.

Generative AI, a subfield of artificial intelligence, focuses on creating
intelligent machines capable of producing content, be it text, images, or
other forms of data, that is indistinguishable from what a human might
generate. It harnesses the power of large language models and deep learning
techniques to produce creative, contextually relevant outputs that hold
immense promise in various industries.

Here are my key learnings from this course in the form of mind maps. I will be
writing explicit posts on each of the below headers with examples later.

## Transformer Architecture

The transformer architecture has revolutionized the field of natural language
processing (NLP) and is now widely used in a variety of NLP tasks.

![Transformer Architecture](./assets/img/posts/transformer_architecture.png)

###### Model Types:

  * **Encoder-only models** are pre-trained with Masked Language Modeling (MLM) and have the same tokens for input and output. They are bidirectional and Autoencoding**** models. Examples of autoencoding models include BERT and ROBERTA. These models are commonly used for tasks like sentiment analysis, named entity recognition, and word classification.
  * **Decoder-only models** are pre-trained using Causal Language Modeling (CLM) and are unidirectional. They are Autoregressive models. An example of an autoregressive model is GPT. These models are typically used for text generation and zero-shot inferences.
  * **Encoder-decoder models** are sequence-to-sequence models that can be used for tasks like translation, text summarization, and question answering. Examples of encoder-decoder models include T5 and BART.

## Common Generative AI Use Cases

Some of the common use cases for which Generative AI is being currently used
are listed below.

  * Chatbots
  * Generate new content
  * Summarize content
  * Translation
  * Generate code
  * Named entity recognition
  * Connecting to real-time data or external data sources

![GenAI use cases](./assets/img/posts/genai-usecases.png)

## Base Gen AI Models

There are plenty of new large language models becoming available every day but
these are the basic models out there right now (October 2023).

  * GPT
  * FLAN-T5
  * PaLM
  * LLaMa
  * BERT
  * BLOOM

![AI models](./assets/img/posts/genai-models.png)

The two most popular model hubs available currently are

  * Hugging Face
  * PyTorch

## Becoming Better at Prompts: Prompt Engineering

Prompt engineering plays a pivotal role in the effectiveness and precision of
natural language processing models, particularly in applications involving
text generation and completion. It involves carefully crafting the input or
instruction given to the model to generate desired and contextually
appropriate responses. The importance of prompt engineering cannot be
overstated.

![Prompt Engineering](./assets/img/posts/genai-promptengg-1024x585.png)

## Challenges with Gen AI

Major current challenges with respect to using Generative AI are

  * Computational (Hardware and Memory)
  * Fine-tuning models
  * Others
    * Missing latest data
    * Mathematical problems
    * Hallucination

![GenAI Challenges](./assets/img/posts/genai-challenges-1024x377.png)

## Gen AI Project Lifecycle

Below are the four key stages of a generative AI project lifecycle:

**1\. Scope**

  * Clearly define the problem or use case for which the generative AI model will be applied.
  * Understand the specific requirements and expectations for the model's performance.

**2\. Select**

  * Determine whether to utilize an existing pre-trained generative AI model or develop a new one from scratch.
  * Consider the suitability of the model's capabilities and limitations for the intended use case.

**3\. Adapt and Align**

  * Employ prompt engineering techniques to refine the model's prompts and instructions for generating desired outputs.
  * Fine-tune the model's parameters and training data to enhance its performance and alignment with the specific task.
  * Incorporate human feedback to continuously improve the model's accuracy and relevance.

**4\. Deploy**

  * Optimize the model for efficient inference and deployment in real-world applications.
  * Integrate the model into existing applications or develop new generative AI-powered applications.
  * Augment the model's capabilities by combining it with other AI techniques and tools.

![GenAI Project Lifecycle](./assets/img/posts/genai-lifecyclev2.png)

## How to evaluate Gen AI Models?

The two widely used metrics to evaluate Gen AI models are

  * BLEU (**B** i**l** ingual **E** valuation **U** nderstudy) 
  * ROUGE (**R** ecall-**O** riented **U** nderstudy for **G** isting **E** valuation).

![Gen AI Model Evaluations](./assets/img/posts/genai-evaluations.png)

## Optimize Models: Reinforcement Learning from Human Feedback (RLHF)

Reinforcement Learning from Human Feedback (RLHF) is a transformative approach
in the field of Generative AI that combines the strengths of human expertise
with machine learning algorithms to enhance the capabilities of AI models like
GPT-3. This technique aims to bridge the gap between AI's understanding of
human preferences and the ability to generate content that aligns more closely
with those preferences.

**Key Principles of RLHF:**

  1. **Feedback Loop** : RLHF establishes a feedback loop where human evaluators provide ratings or feedback on model-generated content. This feedback loop is essential for the model to learn from human preferences and improve its performance.
  2. **Reward Models** : Reward models are created based on the human feedback. These models serve as guides for reinforcement learning, helping the AI model understand what kind of content is considered more desirable or accurate by humans.
  3. **Training and Fine-Tuning** : The AI model is then retrained and fine-tuned using reinforcement learning techniques. It is exposed to various prompts and content generation tasks to improve its performance in line with the provided feedback.

![RLHF](./assets/img/posts/genai-rlhf.png)

## Responsible AI

It is a fundamental concept in the ongoing quest to ensure that AI
technologies benefit society while minimizing potential harm. Responsible AI
goes beyond just creating intelligent machines; it places a significant
emphasis on the ethical, social, and legal considerations that surround AI.

The three areas to primarily focus are

  * Toxicity
  * Hallucinations
  * Intellectual Property Rights Violations

![Responsible AI](./assets/img/posts/genai-responsibleai.png)

* * *

If you found this interesting, you can find more such articles
[here](https://skthetester.github.io/) on quality assurance, test automation,
tools, and processes. Don’t forget to leave your comments here or on X
[@testingchief](https://x.com/testingchief). Thank you!