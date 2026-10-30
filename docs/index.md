---
title: Overview and Setup
description: "AI by Design Part 1: Responsible AI, the evolution of AI at Cisco, and lab setup (Webex token, Google Colab, Hugging Face, LangChain, Ollama)."
chip: "Part 1 of 4"
headline: "AI by Design"
standfirst: "Frameworks, Tools & Innovation. A hands-on lab exploring Generative AI and Collaboration integration, from tokenization and embeddings to RAG, multimodal AI, and beyond."
meta:
  - label: SESSION
    value: Delivered by Omer Ilyas
  - label: STACK
    value: Webex · Google Colab · Hugging Face
  - label: MODULES
    value: Overview · Module 1
  - label: REVISION
    value: v3 · October 2026
links:
  - title: "Google Colab"
    url: https://colab.research.google.com
  - title: "Hugging Face"
    url: https://huggingface.co
  - title: "Webex Developer Portal"
    url: https://developer.webex.com
  - title: "LinkedIn · Omer Ilyas"
    url: https://www.linkedin.com/in/omerilyas4ccie/
---

## About this lab { #about data-toc-label="About this lab" }

<p class="tagline"><del>From using AI</del> <span>to understanding how it is built.</span></p>

In this hands-on lab you go through the fundamental concepts of AI, the techniques behind Generative AI, and how AI can be integrated with Collaboration to create efficient workflows. You start with Cisco's approach to Responsible AI and the evolution of AI at Cisco, set up your lab tools, and then build your way up from tokenization and embeddings to RAG, multimodal AI, GenAI frameworks and open-source models.

The lab has four parts, one page each. This page is **Part 1**: the overview and your lab setup.

### Lab at a glance { #glance data-toc-label="Lab at a glance" }

<div class="glance build" markdown>

| | Module | What you do |
|---|---|---|
|  | [Overview](#module-0) | Responsible AI, the evolution of AI at Cisco, roadmap, and the lab overview |
| 1 | [Pre-Requisites and Setup](#module-1) | Set up your lab environment, API keys, Python tooling, and verify connectivity |

</div>

### How to use this guide { #how-to data-toc-label="How to use this guide" }

Each part of the lab lives on **one page**. Scroll down and work through it in order.

- The **TREE** on the left shows where you are. The progress bar under it fills up as you scroll.
- Press <kbd>J</kbd> / <kbd>K</kbd> to jump to the next or previous section.
- When you finish a task, click **Mark complete** at the end of it. You get a ✓ in the tree, and your progress is saved in this browser.
- Every code block has a **copy** button in its top-right corner. Paste the code into a new Colab cell and run it.
- Click any screenshot to zoom in.

### Key Vault and lab notes { #lab-notes data-toc-label="Key Vault and notes" }

Click **`$ keys`** (bottom-right) to open the **Key Vault**. Paste your Webex Bearer token, Webex Room ID, Hugging Face, LangChain, Pinecone, Gemini and Groq keys there once, and copy them from any page of the lab.

Click **Notes** (bottom-right) to open a scratchpad that stays with you on every part of the lab guide.

!!! warning "Where your keys and notes live"
    The Key Vault and the notes are saved **only in your browser** (localStorage on this device). They are **lost** if you clear your browser data, use a different browser or computer, or open the lab in a private window. On a shared machine, click **Clear All** in the Key Vault and **Clear** in the notes before you log out.

### Your lab proctor { #proctors data-toc-label="Your lab proctor" }

Need help? Raise your hand or reach out to me.

<div class="people" markdown>

<div class="person"><span class="nm">Omer Ilyas</span><span class="rl">Technical Marketing Engineer</span><span class="em">oilyas@cisco.com</span></div>

</div>


<p class="eyebrow">Overview</p>

## Understanding AI and Its Integration with Webex { #module-0 data-toc-label="Overview" }


---

![AI_Info](assets/task1/ai1.png){ loading=lazy }

---

<p class="eyebrow sub">Overview · Task OV1</p>

### Responsible AI Framework { #module-ov1 data-toc-label="ov1 · Responsible AI Framework" data-task="ov1" }


#### Introduction


Artificial Intelligence (AI) is transforming the way we work, enabling innovative solutions and enhancing productivity. Cisco is committed to innovating responsibly, with responsible AI being non-negotiable. Our approach is grounded in the principles of transparency, fairness, accountability, reliability, security, and privacy. Cisco's Responsible AI Framework, aligned with the  AI Risk Management Framework, ensures that all AI initiatives undergo rigorous assessments, particularly around privacy. 

Remember data has value, Cisco's AI strategy emphasizes building ethical and trustworthy systems that mitigate risks while enhancing innovation across products and services.

<!-- ![AI_InfoIMP1](assets/task1/IMP1.png){ loading=lazy } -->
![AI_InfoIMP](assets/task1/IMP.png){ loading=lazy }

Please refer to the below info for more detailed insights about Cisco Responsible AI:

* <a href="https://blogs.cisco.com/news/responsible-ai-is-built-on-a-foundation-of-privacy" target="_blank">Responsible AI is built on a foundation of privacy</a>
* <a href="https://www.cisco.com/c/dam/en_us/about/doing_business/trust-center/docs/cisco-responsible-artificial-intelligence-principles.pdf" target="_blank">Cisco's Responsible Artificial Intelligence Principles</a>
* <a href="https://blogs.cisco.com/security/our-responsible-approach-to-governing-artificial-intelligence" target="_blank">Cisco's Responsible Approach to Governing Artificial Intelligence</a>
* <a href="https://www.cisco.com/c/dam/en_us/about/doing_business/trust-center/docs/cisco-responsible-artificial-intelligence-framework.pdf" target="_blank">Cisco's Responsible Artificial Intelligence Framework</a>

![AI_Info1](assets/task1/raifw.png){ loading=lazy }


<p class="eyebrow sub">Overview · Task OV2</p>

### The Evolution of AI at Cisco { #module-ov2 data-toc-label="ov2 · The Evolution of AI at Cisco" data-task="ov2" }


#### Foundations of Innovation


At Cisco, innovation is woven into the fabric of everything we do. We've been at the forefront of AI development long before it became a buzzword.  Our journey spans decades, from early developments in audio and video intelligence, like echo cancellation, media resilience, to recent breakthroughs like noise removal, face recognition, and immersive experiences, just to name a few. We continue to push boundaries, enhancing AI across multiple domains to deliver immersive and intelligent experiences. Innovation in AI isn't just a trend for us. It's a longstanding commitment to excellence and progress.

![AI_Info12](assets/task1/in_ai.png){ loading=lazy }

What we want everyone to understand is that AI is the core fabric that powers our platforms, enabling  reimagining of work, workspaces, and customer experiences. Whether through the Webex Suite, advanced devices, or   contact center solutions, AI drives the seamless, intelligent, and immersive experiences that define modern collaboration. Cisco's AI-powered Webex platform is designed to transform the way we work, ensuring that every interaction is smarter, more efficient, and more personalized.

![AI_Info122](assets/task1/core.png){ loading=lazy }

In recent years, we've expanded our platform with several new AI capabilities. Here are a few highlights:

> **Disclaimer:** Certain capabilities referenced below may not yet be generally available and are subject to change. Please consult your Cisco representative for current availability and roadmap details.

![AI_Info1223](assets/task1/ai13a.png){ loading=lazy }

![AI_Info1224](assets/task1/ai14a.png){ loading=lazy }

![AI_Info1225](assets/task1/ai15a.png){ loading=lazy }

![AI_Info1226](assets/task1/ai16a.png){ loading=lazy }

![AI_Info1227](assets/task1/ai17a.png){ loading=lazy }

![AI_Info12277](assets/task1/ai20a.png){ loading=lazy }

![AI_Info12277](assets/task1/ai22a.png){ loading=lazy }

![AI_Info12277](assets/task1/ai23a.png){ loading=lazy }

![AI_Info12277](assets/task1/ai24a.png){ loading=lazy }

![AI_Info12277](assets/task1/ai18a.png){ loading=lazy }

![AI_Info122771](assets/task1/ai21a.png){ loading=lazy }

![AI_Info1228](assets/task1/ai19ab.png){ loading=lazy }


<p class="eyebrow sub">Overview · Task OV3</p>

### Roadmap AI Features { #module-ov3 data-toc-label="ov3 · Roadmap AI Features" data-task="ov3" }


#### Upcoming Features


!!! important
        The following slides contain forward-looking statements about AI roadmap features. 
        These features are subject to change without notice based on ongoing research, development, and market needs. 
        Expected delivery dates / feature release are subject to change. 
        
        Please refer to our Safe Harbor Statment.

![AI_Info1229](assets/task1/sh.png){ loading=lazy }

![AI_Info1226](assets/task1/rm2.png){ loading=lazy }

![AI_Info1225](assets/task1/rm3.png){ loading=lazy }

![AI_Info1224](assets/task1/rm4.png){ loading=lazy }


<p class="eyebrow sub">Overview · Task OV4</p>

### Summary { #module-ov4 data-toc-label="ov4 · Summary" data-task="ov4" }


![AI_Info1229](assets/task1/ai20.png){ loading=lazy }

??? note 
    * Our product teams are hosting AI sessions. Please review the agenda and join the ones that interest you.

<p class="eyebrow sub">Overview · Task OV5</p>

### Lab Guide Overview { #module-ov5 data-toc-label="ov5 · Lab Guide Overview" data-task="ov5" }


#### Introduction


=== "Key Takeaways"

    In this lab guide you will go through the fundamental concepts of AI, various techniques, and how AI can be integrated within Collaboration to create efficient workflows.

    !!! important
        
        Upon completion of this lab you will be able to:

        * Understand the basics of AI and its applications
        * Learn about embedding techniques
        * Vector databases
        * Gain insights into Generative AI models
        * Familiarize yourself with different AI frameworks
        * Integrate AI with Webex to create seamless workflows
        * Develop hands-on skills through practical exercises
        * Retrieval Augmented Generation (RAG) and Multimodal RAG
        * Understand Fine-tuning and Quantization (Optional Task)
        * Deploy Fine Tuning techniques (Optional Task)

=== "Key Prerequisites"

    * Basic understanding of AI concepts is helpful but not required.
    * We will be using Google Colab for this lab. However, if you have your own machine with an Nvidia chipset and prefer to run the lab locally, feel free to do so.

=== "Disclaimer"

    !!! important
    
        The lab design and configuration examples provided are for reference/learning purposes only. This is a sample deployment, and not all recommended features are used or enabled optimally. For design-related questions, please contact your representative at Cisco or Cisco Collab TME team.

=== "Lab Tasks Overview - Generative AI and Webex integration"

    * Lab Setup - Google Colab and Hugging Face
    * AI/ML Revolution Unveiled
    * Tokenization
    * Embeddings and Vector Database
    * Context Windows and Retrieval Augmented Generation (RAG)
    * Multimodal RAG
    * Understanding Fine-Tuning for Large Language Models (Optional Task)
    * Fine Tuning - Deep Dive into Quantization , LoRA and SFT (Optional Task)
    * Configuring and Fine Tuning - Using llama2 (Optional Task)
    * Configuring and Fine Tuning - Using llama3 (Optional Task)
    * Configuring and Fine Tuning - Using ChatGPT (Optional Task)
    * Model Merging (Theory Only) (Optional Task)


---

!!! important
    **Ready to begin?** Jump into [Task 1 - Pre-Requisites and Setup](#module-1) to get your lab environment ready.


<p class="eyebrow">Module 1</p>

## Pre-Requisites and Setup { #module-1 data-toc-label="Module 1 · Setup" }


<p class="eyebrow sub">Module 1 · Task 1A</p>

### 🔐 Webex - Getting Bearer Tokens and Room ID { #module-1a data-toc-label="1a · Webex - Getting Bearer Tokens and Room ID" data-task="1a" }


#### Introduction


To interact with Webex programmatically such as sending messages, you’ll need to authenticate using a Webex API access token (Bearer token).
This token will act like a digital key that allows your script to securely access your Webex account and perform actions on your behalf (like sending messages, listing spaces, etc.). Without it, any API call to Webex will be rejected. You can find more information on the Webex Developer Portal <a href="https://developer.webex.com" target="_blank">here.</a>

=== "1. Steps to Obtain and Use Your Webex Token"

    * Log in to the <a href="https://developer.webex.com" target="_blank">Webex Developer Portal</a> and click on Log in.
    
    !!! important
        Remember to use the specific account that you selected for your API keys e.g. **tmedemouserX@gmail.com**, where **X** is the number you were assigned (e.g., 1, 2, etc.). However, since we will be logging into Webex (not Gmail), please replace the domain with **@boldbetz.com**.

        **Example:** 👉 **`tmedemouserX@boldbetz.com`** The password for your assigned account is provided in your **.txt file**.
    
    *    After logging in, click on your profile picture (top-right corner).  Under **"Bearer"**, copy the displayed token as this is the one you’ll use in the upcoming tasks.

    !!! tip "Save to Key Vault"
        Click the **`$ keys`** button (bottom-right of this page) to open the Key Vault panel and paste your **Webex Bearer Token** there. It will be available on all lab pages.

    ![Wbx2](assets/task1/wbx2.png){ loading=lazy }

    * Use your assigned tmedemouserX@boldbetz.com account to log in to the Webex App that is pre-installed on your laptop. If your laptop doesn't have the Webex App, browse to <a href="https://web.webex.com" target="_blank">web.webex.com</a> and log in there with the same account.
    ??? note 
        Remember to use the specific account that you selected for your API keys e.g.tmedemouserX@gmail.com, where X is the number you were assigned (e.g., 1, 2, etc.). 

    * Once logged in, create a new Webex Space and name it something like "Webex AI Lab".

    ![Wbx3](assets/task1/wbx3.png){ loading=lazy }

    * After the space is created, we will retrieve its  ID, this will be used in a later step in the lab guide (Task 6a).

    * Now, go back to the <a href="https://developer.webex.com" target="_blank">Webex Developer Portal</a>l and log in again.

    * Click on Documentation → Webex Messaging.

    ![Wbx4](assets/task1/wbx4.png){ loading=lazy }

    * Select All APIs, then navigate to Rooms → List Rooms, and press Run.

    ![Wbx5](assets/task1/wbx5.png){ loading=lazy }

    * In the response, you will find a list of rooms associated with your account. Locate the room you just created (e.g., "Webex AI Lab") and copy its corresponding ID. This will be used in a later step in the lab guide (Task 6a).

    !!! tip "Save to Key Vault"
        Open the **`$ keys`** panel (bottom-right) and paste your **Webex Room ID** there for easy access later.

    ![Wbx6](assets/task1/wbx6.png){ loading=lazy }


### Pre-Requisites and Setup (Optional Steps)


!!! note

    The following steps are provided for your information only. Since you've already received the necessary API keys (which were pre-generated and provided to you as a .txt file), there's no need to follow these instructions during the lab. However, if you're interested in learning how to create the API keys yourself, feel free to review the steps below. We've pre-created the keys to save time during the session.

    ⚠️ Note: Unlike static API keys, Webex access tokens expire periodically. Therefore, you’ll need to follow the steps above to retrieve a fresh token each time you want to use the Webex APIs.


<p class="eyebrow sub">Module 1 · Task 1B</p>

### 🧪 Google Colab - Accessing Google Colab and creating account { #module-1b data-toc-label="1b · Google Colab - Accessing Google Colab and creating account" data-task="1b" }


#### Introduction


=== "1. How to Use"

    Google Colab is one of several, cloud-based platform that provides a convenient environment for running notebooks. If you want to create a machine learning model but don't have a computer that can handle the workload, Google Colab is the platform for you. In our lab, we will be using Google Colab to test and run our code. However, if you have your own Python environment and prefer to run the code on your local machine, please feel free to do so.

    Here are some reasons why using Google Colab can be beneficial for this lab:

    * Free Access to GPUs and TPUs: Google Colab offers free access to powerful GPUs and TPUs, which can significantly accelerate the training and fine-tuning of machine learning models.
    * No Setup Required: With Colab, there is no need to set up your local environment. Everything runs in the cloud, which saves time and avoids configuration issues.
    * Easy Collaboration: Colab notebooks can be easily shared and collaborated on with team members, making it an ideal tool for collaborative projects.
    * Integration with Google Drive: Colab integrates seamlessly with Google Drive, allowing you to save and manage your work conveniently.
    * Pre-installed Libraries: Many popular machine learning libraries, including TensorFlow and PyTorch, come pre-installed in Colab, making it easy to start working on your projects immediately.




=== "2. Getting Started With Google Colab"

    !!! warning "Session Timeout"
        When using Google Colab, if your notebook is **idle for too long**, the session will **time out**, requiring you to **re-run all the cells from the start**.

    
    === "1. Initial Step"
        To start working with Google Collab Notebook you first need to log in to your personal Google account, then go to this link <a href="https://colab.research.google.com" target="_blank">Google Colab</a>

        !!! Note
            You can use your personal Google account(gmail) for your lab


    === "2. New Jupyter Notebook"
        * Create a new Jupyter Notebook

         ![Colab_SignUP](assets/task1/Colab_signup.png){ loading=lazy }
         
        * On creating a new notebook, it will create a Jupyter notebook with Untitled0.ipynb and save it to your google drive in a folder named Colab Notebooks. Now as it is essentially a Jupyter Notebook, all commands of Jupyter Notebooks will work here. 

         ![Colab_Untitled](assets/task1/Colab_unt.png){ loading=lazy }

        ??? note
            * There might be times when we need to fine-tune models or perform specific tasks that require changing the runtime environment in Colab. Google Colab offers different runtime environments that can be selected based on your requirements:
          
            * **Python Versions:** You can select between different versions of Python (e.g., Python 2 or Python 3)depending on the compatibility of the code and libraries. We will be using Python3 for our lab.
            
            * **Hardware Accelerators:** Colab provides access to hardware accelerators, which can be particularly useful for intensive computations. You can choose between:
                ```
                None: No hardware acceleration, suitable for basic tasks.
                GPU: Accelerate your computations with a Graphics Processing Unit.
                TPU: Use a Tensor Processing Unit for even faster performance, especially beneficial for deep learning tasks.
                ```

        * Click the arrow next to “Connect” to open the dropdown

            ![Colab_runtime](assets/task1/Colab_chg.png){ loading=lazy }

        * Select “Change runtime type”: This will open a dialog box where you can configure the runtime environment.
        
          * Select Python Version: Choose Python 3 from the “Runtime type” dropdown menu.

          * Select Hardware Accelerator: From the “Hardware accelerator” dropdown menu, choose  GPU, or TPU .

        ??? note 

            * GPU (Graphics Processing Unit): Best for tasks requiring extensive parallel processing, such as training neural networks (the main focus in our lab guide).

            * TPU (Tensor Processing Unit): Optimized for deep learning tasks

        ![Colab_savruntime](assets/task1/savColab_chg.png){ loading=lazy }

        * Save Settings: Click “Save” to apply the changes.

        ??? note 

            * **New Cell:** Whenever you want to copy the code in Google Colab and run it, be sure to click on + Code to add a new code cell.
            
            ![Colab_newcell](assets/task8/newcell.png){ loading=lazy }

            * **Execute Code:** Click the play button to the left of the code, or use the keyboard shortcut "Command/Ctrl+Enter" while the cell is selected.
            
            ![Colab_newcell_execute](assets/task8/exec.png){ loading=lazy }
            

    === "3. GPU and TPU Information"

        While Google Colab offers free access to GPUs and TPUs, there are limitations. For more consistent access to high-performance GPUs and TPUs, you might need to subscribe to <a href="https://colab.research.google.com/signup" target="_blank">Colab Pro or Colab Pro+ accounts</a>. These paid plans provide priority access to better hardware, longer runtimes, and more memory.
    
        <p align="right"> 👉 When you're ready, click the <strong>“Huggingface Hub - Creating Account”</strong> tab below to proceed. </p>


<p class="eyebrow sub">Module 1 · Task 1C</p>

### 🤗 Huggingface Hub - Creating Account { #module-1c data-toc-label="1c · Huggingface Hub - Creating Account" data-task="1c" }


#### Introduction - Using Huggingface Hub to share our Datasets


In this lab, we will be utilizing the [Hugging Face Hub](https://huggingface.co/) to load our custom datasets (Optional Task). As we progress, we will be working with datasets, so let’s create a Hugging Face account to facilitate our lab exercises. Hugging Face provides an extensive repository of datasets that can be easily integrated into your machine learning workflows. For the purposes of this lab, we will demonstrate how to access/upload and use our custom datasets effectively.

However, when fine-tuning models in your own work environment, especially if you are using private data, there are important considerations to keep in mind:

* **Private Datastores:** If you are working with proprietary or sensitive data, it is crucial to use your organization's secure datastores. Ensure that all data handling complies with your organization's data privacy policies and regulations.
* **Hugging Face Datasets:** If you prefer to use Hugging Face for dataset storage and management, make sure to mark your datasets as private. This setting ensures that your data cannot be accessed by anyone outside your organization, maintaining the confidentiality and integrity of your information. Please refer to Huggingface documentation for more info.

**Few more Condsideration**

* **Upload Dataset:** When uploading your dataset to Hugging Face, choose the appropriate privacy settings. You can set your dataset to private during the upload process.
* **Check Permissions:** Regularly review and manage the permissions of your datasets to ensure they remain private and secure.
* **Collaborator Access:** If you need to share the dataset with specific team members, use the Hugging Face interface to grant access to trusted collaborators only.

By following these guidelines, you can ensure that your data remains secure while leveraging the powerful tools and resources provided by Hugging Face. This approach not only enhances your workflow efficiency but also upholds the best practices in data security and privacy.

=== "1. Accessing Hugging Face"

    Hugging Face can be accessed by browsing to <a href="https://huggingface.co/" target="_blank">huggingface</a>
    
    ![HLF](assets/task8a/HF.png){ loading=lazy }


=== "2. Signing Up & Creating Account"

    * Browse to Hugging Face home page and click on Sign up. Follow the instructions as per below images

    ![SignUP](assets/task8a/signup.png){ loading=lazy }

    ![Prof](assets/task8a/HFProfile.png){ loading=lazy }

    * Please check your email address for a confirmation link and click to verify your account 

    ![Verify](assets/task8a/HFverify.png){ loading=lazy }

    * Organization Creation (Optional): While you can upload datasets and fine-tune models directly on Hugging Face without creating an organization, you have the option to create an organization on Hugging Face. This can be particularly useful for team collaboration, as it allows you to upload all your datasets and models in one centralized location. Click on "Create a New organization". In our example, we're creating an organization called <span class="colour" style="color:red">OmerAccount</span>. If that name is already taken, please choose another name of your preference.

    ![Optional](assets/task8a/HFOptional.png){ loading=lazy }

    * Access Your Models and Datasets: The same can be accessed by clicking your profile picture on the top right corner of the Hugging Face website. This will take you to your personal dashboard where you can view and manage your models and datasets.

    ![Mo_DS1](assets/task8a/HFNoMD1.png){ loading=lazy }

    *  At this stage, you will see no models or datasets created under your account.

    ![Mo_DS](assets/task8a/HFNoMD.png){ loading=lazy }


=== "3. Hugging Face API Keys"

    * **Create an API Key:** Sine we will be uploading our datasets to the Hugging Face Hub, we need to create an API key for our account. This API key will be used to authenticate and interact with the Hugging Face services programmatically. You can browse to [huggingface API Key](https://huggingface.co/settings/token)

    or 

    * Click on your profile picture > Settings > Access Tokens

    ![HF_API](assets/task8a/HF_APi.png){ loading=lazy }

    ![HF_WT](assets/task8a/writetoken.png){ loading=lazy }

    * Under the "Access Tokens" section, click on "Create new token." You will see options to select the token type and provide a token name. For example, you might name your token "OmerToken" and select the approperiate permissions.  

        * Fine-grained: tokens with this role can be used to provide fine-grained access to specific resources, such as a specific model or models in a specific organization. This type of token is useful in production environments, as you can use your own token without sharing access to all your resources.

        * Read: tokens with this role can only be used to provide read access to repositories you could read. That includes public and private repositories that you, or an organization you’re a member of, own. Use this role if you only need to read content from the Hugging Face Hub 
        (e.g. when downloading private models or doing inference).

        * Write: tokens with this role additionally grant write access to the repositories you have write access to. Use this token if you need to create or push content to a repository (e.g., when training a model or modifying a model card).

    * As we have a lab envoirnment we will be using the "Write" permission. This token will have read and write access to all your resources and can make calls to inference API on your behalf, as shown in the image below.

    ![HF_CT](assets/task8a/createtoken.png){ loading=lazy }

    * **Save and Secure the Token:** Once the token is generated, save it securely, as it will be needed to access and manage your datasets via the API. The image below is for reference only. Make sure to use and save the token you generate.

    !!! tip "Save to Key Vault"
        Open the **`$ keys`** panel (bottom-right) and paste your **Hugging Face Token** there.

    ![HF_GT](assets/task8a/gentoken.png){ loading=lazy }


=== "4. Accessing Hugging Face in Colab"

    * Open the Google Colab notebook and navigate to the new “Secrets” section in the sidebar by clicking the "key icon”

    ![HF_GT_sec](assets/task8a/gensec.png){ loading=lazy }

    * Click on “Add a new secret.” Enter the name example: HF_TOKEN and value of the secret. Note: The name is permanent once set. 

    * The list of secrets is global across all your notebooks.

    * Use the “Notebook access” toggle to grant or revoke access to a secret for each notebook.

    ![HF_GT_sec_created](assets/task8a/addsec.png){ loading=lazy }


    <p align="right"> 👉 When you're ready, click the <strong>“langchain”</strong> tab below to proceed. </p>

=== "5. Optional Steps (Python Environment)"
    
    ??? note 
    
        * For Python modules requiring API keys as environment variables, you can use the below code snippet:

        The below code snippet is for reference only; there's no need to execute it at this point.

        ```py linenums="1"
        # Import Colab Secrets userdata module

        from google.colab import userdata
        import os

        # Set other API keys similarly
        os.environ["HF_TOKEN"] = userdata.get('HF_TOKEN')
        ```
    <p align="right"> 👉 When you're ready, click the <strong>“Langchain”</strong> tab below to proceed. </p>


<p class="eyebrow sub">Module 1 · Task 1D</p>

### 🔗🔗🔗 LangChain { #module-1d data-toc-label="1d · LangChain" data-task="1d" }


#### Introduction - Using Langchain


=== "1. Getting Started"

    LangChain is a framework that enables developers to build applications using large language models (LLMs). It connects with various AI models, data sources, and APIs, allowing the creation of complex work flows for tasks such as question answering, chatbot interactions, and document summarization. We will explore LangChain in more detail in the later section.
    
    Let's explore how to create a LangChain account and obtain the API key, which we will use later in our lab. 
    
    To start building applications with LangChain, you'll need an API key. This key allows your applications to securely connect with LangChain's services, ensuring proper authentication and usage tracking.

    Lets start by visiting the official <a href="https://smith.langchain.com/settings" target="_blank">LangChain website</a> and create an account. You'll need to enter some basic information about yourself or your organization. In this example, I will be using my Google account (tmedemouserX) to sign up.
    
    ![ls1](assets/task1/ls1.png){ loading=lazy }


=== "2. LangChain API Keys"

    * To create an API key head to the **Settings** page. Then click Create API Key.

    ![ls2](assets/task1/ls2.png){ loading=lazy }

    ![ls3](assets/task1/ls3.png){ loading=lazy }
    
    * Lets create a Personal Access Token

    ![lsr3](assets/task1/lsr3.png){ loading=lazy }

    ??? note
        After generating the token, store it securely, as you will need it for future tasks. Ensure you use and save the token you create.

    !!! tip "Save to Key Vault"
        Open the **`$ keys`** panel (bottom-right) and paste your **LangChain API Key** there.
    

=== "3. LangServe"          

    ??? note 
        The below code snippet is for reference only, there's no need to execute it at this point.  
      
        In the code test snippet below, we'll configure our environment to enable tracing of AI calls and set up the API key for interacting with LangChain's services. We will be using these in the upcoming section.
        ```py linenums="1"
            !pip install -U langchain langchain-openai
            !pip install langchain-community
            export LANGCHAIN_TRACING_V2=true
            export LANGCHAIN_API_KEY=<your-api-key>
        ```
    <p align="right"> 👉 When you're ready, click the <strong>"Ollama - Running Locally - Optional Task"</strong> tab below to proceed. </p>


<p class="eyebrow sub">Module 1 · Task 1E</p>

### 💻 Ollama - Running Locally - Optional Task { #module-1e data-toc-label="1e · Ollama - Running Locally - Optional Task" data-task="1e" }


#### Introduction


Have you ever used ChatGPT and amazed at its ability to understand and respond to your queries? But did you know that you can also harness the power of open-source models using Ollama? With Ollama, you can download and interact with these models directly, getting responses that are tailored to your needs.

In this lab, I'll show you how to install Ollama locally on your machine and start using it to generate responses. You'll learn how to download and load open-source models, and then use Ollama's intuitive interface to interact with them. More info for <a href="https://ollama.com/" target="_blank">Ollama can be found here</a>

??? note
    The steps below are provided for informational purposes. If you are using the demo laptop in this lab, feel free to follow these instructions. However, if you are using your personal or work machine, please ensure that you have the necessary privileges and authorization from your organization's administrator to install Ollama locally.


=== "1. Prerequisites"
    
    * Ensure that Docker is installed and running on your machine. It is available for various operating systems, including macOS, Windows, and Linux. You can download it from the <a href="https://www.docker.com/" target="_blank">official Docker website</a> and follow the installation instructions for your specific OS.


=== "2. Installing Ollama Locally"

    ??? note
        Since we're using a Mac, I'll demonstrate how you can install it on macOS.
    
    * First, you need to install Ollama. You can download it <a href="https://ollama.com" target="_blank">here</a> and clicking on the download button. Follow the instructions.

    * Once installed, Ollama functions as a command-line application, allowing you to interact with it directly through the terminal. To get started, open the terminal and enter the following command:

    ``` py linenums="1" title="SHELL"
    ollama
    ```

    * It will output the below commands
    
    ![Ollama](assets/task1/olama.png){ loading=lazy }

    * Ollama supports a list of models available <a href="https://ollama.com/library" target="_blank">here</a>. Below are some example models that can be downloaded:

    ![Ollama1](assets/task1/olama1.png){ loading=lazy }

    * To download a model, for example, gemma:2b, which is a lighter model, we can simply type:

    ``` py title="SHELL"
    ollama pull gemma:2b
    ```

    ![pull](assets/task1/pull.png){ loading=lazy }

    * After pulling the model we can interact with it in the terminal by typing:

    ``` py title="SHELL"
    ollama run gemma:2b
    ```

    ![pull1](assets/task1/pull1.png){ loading=lazy }

    * We can now ask our question directly in the terminal

    ![pull2](assets/task1/pull2.png){ loading=lazy }

    * To remove model you can type

    ``` py title="SHELL"
    ollama rm gemma:2b
    ```

    * To see the models installed, just enter 

    ``` py title="SHELL"
    ollama list
    ```

=== "3. Ollama - Web Interface"
    
    ??? note
        Docker must be installed beforehand as a prerequisite.

    Once we've installed Ollama, we can interact with it directly through the terminal, as demonstrated earlier. But what if you prefer a web interface? There are several open-source tools available, but I'll show you how to use <a href="https://github.com/open-webui/open-webui" target="_blank">Open WebUI</a>, which was previously known as Ollama WebUI.

    Open WebUI is a versatile, feature-rich, and user-friendly web interface that you can host yourself and use entirely offline. It offers a ChatGPT-style interface, allowing you to interact with language models running on locally (Ollama). This tool is especially useful for those who want to run language models locally or in a self-hosted environment, ensuring both data privacy and control.

    * After installing Ollama, simply run the following Docker command to set up the interface

    ``` py title="SHELL"
    docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
    ```

    ![pull3](assets/task1/pull3.png){ loading=lazy }

    * Once installed, you can access Open WebUI at <a href="http://localhost:3000" target="_blank">localhost</a>. 

    <span style="color: RED;">Note: Before accessing the web interface, you will be prompted to create an account. Please follow the instructions.</span>

    * In the dropdown menu, you'll see the model you previously installed via the terminal (gemma:2b).

    ![pull4](assets/task1/pull4.png){ loading=lazy }

    * You can now Interact with the model via WebUi

    ![pull5](assets/task1/pull5.png){ loading=lazy }

    * You no longer need to use the terminal to download a model. Simply navigate to the “Settings --> Models” section in the WebUI, and select the specific model you want to download.

    ![pull6](assets/task1/pull6.png){ loading=lazy }

    * After installing, all the installed models will be displayed in the UI.

    ![pull7](assets/task1/pull7.png){ loading=lazy }

    ??? note
        Using LangChain with Ollama allows you to leverage Ollama's capabilities within the LangChain ecosystem. You can find <a href="https://python.langchain.com/v0.1/docs/get_started/quickstart/" target="_blank">more information here

    <p align="right"> 👉 This concludes the task. Click the <strong>"AI/ML Revolution Unveiled "</strong> Task on the left. </p>


<a class="next-card" href="part-2/">
  <span class="nc-k">Next · Part 2</span>
  <span class="nc-t">AI Foundations: Tokens, Embeddings & Vectors</span>
  <span class="nc-u">Part 2 →</span>
</a>
