#Computerized Virtual Psychotherapy
**CS199, Fall 2016**

**Wan Di Liu**

**Advised by Professor L. Kleinrock**

**Dec 13, 2016**

###IRI Statement
The purpose of my project is to create a computational model for psychotherapy conversations.

###Project Goals and Timeline
![Project Timeline Overview](https://github.com/wandiliu/El/blob/master/IRI%20timeline.jpg)
####Fall 2016
#####Stage 1
I set my year-end goal as to create a minimal-working retrieval model for basic psychotherapy purposes. This model is built on top of Christina Cacioppo's Ellie implementation of Eliza, an early conversation model created in the 1960s by MIT's Joseph Weizenbaum. It will try to incorporate the 5 psycholinguistic features that were shown to predict therapy success, as noted in Tim Althoff, Kevin Clark, and Jure Leskovec's paper for Stanford's Counseling Conversation Analysis Project. I also decided on Crisis Text Line's Enclave Data as my primary source of data, chosen for its large corpus and robust structured-text data schema. I now divided my attention to 1) the retrieval model, and 2) the data application.

#####Stage 2
The retrieval model had its basic backbone on Github, so I only needed to comprehend its core source code and revise it according to the linguistic features that I needed to incorporate. In this stage, I performed an analysis of the paper by Althoff, Clark, and Leskovec, and decided on the manners in which I will manually embed the features that contributed to psychotherapy success (more on this in source code report). On the other hand, I coordinated with Fabien and secured him as the principal investigator for my IRB and Enclave Data application, who will apply for and process the data for me.

#####Stage 3
In the final stage of this course, I reached out to Enclave Data's data science team hoping for some advice on my project and data application. Nitya, the open data manager for Crisis Text Line, replied to me and generously explained the vision of CTL and the main goals of the Enclave Data initiative. I informed her of my ideas for this project, and she encouraged me to apply. Meanwhile, I have submitted the IRB application, and have began my CTL data application, which I plan to submit before Christmas.

####Winter 2017
For the winter quarter, I plan on continuing with the development of my model. A major setback in my minimal retrieval model was the lack of context in the counselor responses, which, as pointed out by [Althoff *et al.*](http://timalthoff.com/docs/althoff-2016-mental_health.pdf), is an important factor for the success of crisis counseling. I will research attention mechanisms that assist in contextualization and summarization during conversations, and refer to the works of [Rush *et al.*](https://arxiv.org/abs/1509.00685v2), as well as existing projects which utilize attention vectors, such as [Neural Machine Translation](https://github.com/tuzhaopeng/NMT) and an [Attention-based summarization model](https://github.com/falcondai/trained-ABS-model). I will train my network with the IMDB corpus, which contains natural language conversations in a variety of film genres. 

Meanwhile, I will hopefully have received the IRB approval. 

####Spring 2017
In March, I will be informed of my Enclave Data application results. 
- If I am granted with the data access. I will first allocate around 2 weeks to set up the data in the IRI lab, then spend 1 week, with the assistance of Fabien, process and extract all data variables required for my model. I will then start training the data, finetuning its features for about 4 weeks. If authorized, I will take the model online and create a web chatroom interface that others can use to test the model.
- If the application is denied, I will need to select a different corpus as my training data, and revisit my project statement to transition to another topic. For example:
  - Using the IMDB corpus, create a day-to-day natural language chabot to provide social interaction and intellectual practice for the elderly population as a means of Alzheimer prevention
  - Using voluntarily-collected Facebook messenger conversations, seek to solve the problem of "inconsistency" that lies in generative networks, and trying to mimic traits of "identity" and "personality"

I will end my IRI project with a final paper that also serves as the IRB closure report, and present my model at the year-end presentation.

####Quarterly Summary
#####Activities & Accomplishments 
After meeting with fellow participants and mentors at the kickoff, I created a project pipeline and discussed it with my mentor, Dr. Eric Haseltine. At the same time, I enrolled in an independent research course under Professor Kleinrock, and discussed my project my research advisor, Professor Fabien Scalzo. 

#####What I Learned

#####Barriers

####Performance Evaluation


####
