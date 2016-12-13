####Linguistic features to be included:

#####Adaptability 
> "*successful counselors are more sensitive to the current trajecory of the conversation and react accordingly"*

This feature suggests that counselors often use similar language at the beginning of conversations, but pay attention to the flow and progress of their specific conversation by varying their language in the latter stages of the conversation to rememdy poor conversations. I will attempt to incorporate the factor of Adaptability through a combined implementation with the Progress feature, which will be mentioned below. This will rely on my intuition as a past counselor at 7Cups, and I will try to create a set of responses that tailor best to the given situation. However, because attention is not taken into perspective (a significant drawback to retrieval models), I will be unable to accurately predict the success of a conversation at any given point through the entire previous dialogue --  I can only attempt to capture the flow of the conversation through keywords at the most-current exchanges. The Adaptability feature suggests the importance of incorporating context in the situations crisis counseling. This further highlights the importance of implementing a more advanced model. 


#####Clarification
> *"successful counselors **clarify** situations by writing more, reflect back to check understanding, and making their conversation partners more comfortable through affirmation"*

This feature, also known as "echoing", is one of the easier methods to imitate. I will 


#####Creativity
> *"successful counselors respond in a more creative way, not directly repeating the patients' words and not using generic, formatted responses"*

Ideally, counselor creativity can be best imitated through a seq2seq network that is capable of creating novel responses from a generic corpus. Unfortunately, this is another ideal that cannot be implemented by the primitive retrieval model. Given its nature, it can only generate an output from a fixed set of reponses. In this retrieval model, my solution is, given a keyword, to associate responses to it that do not use directly repeat the keyword but approach its issue through paraphrasing. I will also implement creativity intuitively, utilizing more verbal responses, as the SMS setting is more forgiving of institutional talk and allows for the blending of informality. 

#####Progress
> *"successful counselors are quicker to get to know the core issue and faster to move on to collaboratively solving the problem"*

Again, this 

#####Keywords
  -	  Successful counselors are able to direct the texter in a positive direction to encourage positive sentiments
  
  - implement "hedges, check questions, and unique talk style (no coordination)
