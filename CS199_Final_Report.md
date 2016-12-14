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
The retrieval model had its basic backbone on Github, so I only needed to interpret its core source code and revise it according to the linguistic features that I needed to incorporate. In this stage, I performed an analysis of the paper by Althoff, Clark, and Leskovec, and decided on the manners in which I will manually embed the features that contributed to psychotherapy success (more on this [here](https://github.com/wandiliu/El/blob/master/plugins/el/README.md)). On the other hand, I coordinated with Fabien and secured him as the principal investigator for my IRB and Enclave Data application, who will apply for and process the data for this project.


#####Stage 3
In the final stage of this course, I reached out to Enclave Data's data science team, hoping for some advice on my project and data application. Nitya, the open data manager for Crisis Text Line, replied to me and generously explained the vision of CTL and the chief goal of the Enclave Data initiative. I informed her of my ideas for this project, and she encouraged me to apply. Meanwhile, I have submitted the IRB application, and have began my CTL data application, which I plan to submit before Christmas.


####Winter 2017
For the winter quarter, I plan on continuing with the development of my model. A major setback in my minimal retrieval model was the lack of context in the counselor responses, which, as pointed out by [Althoff *et al.*](http://timalthoff.com/docs/althoff-2016-mental_health.pdf), is an important factor for the success of crisis counseling. I will research attention mechanisms that assist in the contextualization and summarization of conversations, and refer to the works of [Rush *et al.*](https://arxiv.org/abs/1509.00685v2), as well as existing projects which utilize attention vectors, such as [Neural Machine Translation](https://github.com/tuzhaopeng/NMT) and an [Attention-based summarization model](https://github.com/falcondai/trained-ABS-model). I will train my network with the IMDB corpus, which contains natural language conversations in a variety of film genres. 


Meanwhile, I will hopefully have received the IRB approval. 


####Spring 2017
In March, I will be informed of my Enclave Data application results. 
- If I am granted data access, I will first allocate around 2 weeks to set up the data in the IRI lab, then spend 1 week, with the assistance of Fabien, to process and extract all data variables required for my model. I will then start training the data, fine tuning its features for about 4 weeks. If authorized, I will take the model online and create a web chatroom interface that others can use to test the model.
- If the application is denied, I will need to select a different corpus as my training data, and revisit my project statement to transition to another topic. For example:
  - Using the IMDB corpus, create a day-to-day natural language chabot to provide social interaction and intellectual practice for the elderly population as a means of Alzheimer prevention
  - Using voluntarily-collected Facebook messenger conversations, seek to solve the problem of "inconsistency" that lies in generative networks, and try to establish traits of "identity" and "personality" using single-source data


I will end my IRI project with a final paper that also serves as the IRB closure report, and present my model at the year-end presentation.


###Quarterly Summary
####Activities & Accomplishments 
After meeting with fellow participants and mentors at the kickoff, I created a [project pipeline](https://github.com/wandiliu/El/blob/master/IRI_pipeline.pdf) and discussed it with my mentor, Dr. Eric Haseltine. At the same time, I enrolled in an independent research course under Professor Kleinrock. When I recognized that I needed a postgrad-level researcher's help in obtaining data, I spoke to my research advisor, Professor Fabien Scalzo, and received his assistance. My activities this quarter was summarized above, with the two themes being:
  1.  the progression of my Crisis Text Line data application, and 
  2.  the minimal-working retrieval model, [El](https://github.com/wandiliu/El/tree/master/plugins/el), for which I was able to incorporate several [linguistic features](https://github.com/wandiliu/El/blob/master/plugins/el/README.md) discovered by a past researcher's analysis on CTL data. 


####What I Learned
The two key things that I learned from this experience was correspondence and analysis. 

Correspondence wise, I was required to schedule meetings and consult with many different parties in order to progress in my agenda. I was challenged to shuffle between perseverance and compromise, to be adaptable with timelines, milestones, and corpora while standing firm in my vision - to creating conversational AIs that can assist people in need. I learned to correspond efficiently, and be unapologetic with my requests when the circumstance called for progress. I also learned to act on behalf of an institution when reaching out to outside organizations. Independent research have taught me to be flexible in my mitigations, yet keeping my eyes on the prize. 

Analysis wise, I was first presented with the task of analysing my own situation; analysing my own resources, time, and goals led me to creating a reasonable timeline while leaving room for changes and extensions. Then, I was able to analyze and dissect a complete conversation model, from backbone (Eliza) to API (Slack), which taught me the components I needed for my own project. In my implementation of [El](https://github.com/wandiliu/El/blob/master/plugins/el/el.py), I incorporated the counseling strategies verbally, revisiting my own experiences as a crisis intervention volunteer, as well as finding outside research to support these strategies. I learned to design and execute, meanwhile keeping track of inspirations and logging my experience. 

Overall, this independent research course strengthened my communication, analytical, as well as planning skills. I learned to seek help and coordinate, interpret and investigate, all the while keeping my eyes on the “bigger picture”. 


####Barriers
I encountered several barriers throughout this quarter, in the data application as well as in the retrieval model implementation. 

#####Data Application
  1.  My first barrier was the Enclave Data policy, which forbid undergraduate researchers from directly processing and accessing the data. My resolution was to seek help from my advisor, Fabien Scalzo, who agreed to help me obtain and process the data. Were it not for his help, I would have resorted to using another corpus, possibly shifting my research topic altogether, as Crisis Text Line is the only known organization that provides an abundance of counseling data.

  2.  My second barrier was determining whether my vision for my project - a chatbot - aligned with the vision of the CTL Data Review Board. Therefore, I voiced my questions to the data science team. After corresponding with the Open Data Manager, I realized that although my project does not align exactly with the goals of CTL, I am now aware of the many implications of real-user-trained chatbots and the sensitive components that I must take into account when training my model. While I am going to make compromises to my model in the data application, I am nevertheless prepared to move to another data source if my application is not approved. 

#####Retrieval Model

As I started implementing the 5 linguistic features into [El](https://github.com/wandiliu/El/blob/master/plugins/el/el.py), I realized that many important conversation strategies, such as paying attention to the progress of the conversation, as well as the length and sentiment of the responses cannot be achieved with a simple keyword-based retrieval model. Through my [analysis](https://github.com/wandiliu/El/blob/master/plugins/el/README.md), I also realized that context is extremely important in crisis counseling. Certain features, such as response length and sentiment, could be incorporated into the model through a ```response_len``` variable and a parser; unfortunately, I was unable to implement them due to a shortage of time. Therefore, I decided to further establish these features in the neural model next quarter.

###Performance Evaluation
I believe that I have performed satisfactorily in the past 3 months, and is on the right track for winter quarter. However, I do wish that I had taken a less rigorous courseload (6) during Fall quarter, and had allocated more time for my retrieval model. Although it is a working model, I am seeing how it could be further improved in other ways - such as adding response_length variables, and importing other modules such as NLTK to speed up preprocessing. Therefore, I aim to devote more time to the neural model in the upcoming quarter, and transcend my performance in the past 3 months. I also wish that I had spent more time researching other projects, and learning a new programming language. Due to my unfamiliarity with other languages I was rushed to settle with the source code that was implemented in Python. I believe that in order for me to create a better neural model, I need to overlook the factor of syntax, and instead focus on the model’s own functionality. Therefore, I will choose a more appropriate model over one in a familiar language, even if it means sacrificing time to learn the syntax itself. 


####




