| #Principle | Prompt Principle | Example Prompts |
|------------|------------------| ---------------------|
| 1          | Integrate the intended audience in the prompt | Construct an overview of how smartphones work, intended for seniors who have never used one before. |
| 2          | Employ affirmative directives such as "do," while steering clear of negative language like "don’t." | How do buildings remain stable during earthquakes? |
| 3          | Implement example-driven prompting (Use few-shot prompting) | Example 1: Translate the following English sentence to French: \"The sky is blue.\" (Response: \"Le ciel est bleu.\")\nExample 2: Translate the following English sentence to Spanish: \"I love books.\" (Response: \"Amo los libros.\") |
| 4          | When you need clarity or a deeper understanding of a topic, idea, or any piece of information, utilize the following prompts:<br>- Explain [insert specific topic] in simple terms.<br>- Explain to me like I'm 11 years old<br>- Explain to me as if I'm a beginner in [field]<br>- Explain to me as if I'm an expert in [field]<br>- “Write the [essay/text/paragraph] using simple English like you’re explaining something to a 5-year-old” | Explain to me like I'm 11 years old: how does encryption work? |
| 5          | When you want to initiate or continue a text using specific words, phrases, or sentences, utilize the following prompt:<br>- I'm providing you with the beginning [song lyrics/story/paragraph/essay...]:<br> [Insert lyrics/words/sentence]. Finish it based on the words provided. Keep the flow consistent. | "The misty mountains held secrets no man knew.\" I'm providing you with the beginning of a fantasy tale. Finish it based on the words above. |
| 6          | Use output primers, which involve concluding your prompt with the beginning of the desired output. Utilize output primers by ending your prompt with the start of the anticipated response | Describe the principle behind Newton's First Law of Motion. Explanation: | 
| 7          | To write any text, such as an essay or paragraph, that is intended to be similar to a provided sample, include the following instructions:<br>- “Please use the same language based on the provided paragraph[/title/text/essay/answer]” | "The gentle waves whispered tales of old to the silvery sands, each story a fleeting memory of epochs gone by.\"\nPlease use the same language based on the provided text to portray a mountain's interaction with the wind. |
| 8          | When formatting your prompt, start with '###Instruction###', followed by either '###Example###' or '###Question###' if relevant. Subsequently, present your content. Use one or more line breaks to separate instructions, examples, questions, context, and input data |
| 9          | Incorporate the following phrases: “Your task is” and “You MUST” |
| 10         | Incorporate the following phrases: “You will be penalized” |
| 11         | Use the phrase "Answer a question given in natural, human-like manner" in your prompts |
| 12         | Break down complex tasks into a sequence of simpler prompts in an interactive conversation |
| 13         | Clearly state the requirements that the model must follow in order to produce content, in the form of the keywords, regulations, hint, or instructions |
| 14         | Use Leading words like writing “think step by step” |
| 15         | Add to your prompt the following phrase “Ensure that your answer is unbiased and does not rely on stereotypes” |
| 16         | Allow the model to elicit precise details and requirements from you by asking you questions until it has enough information to provide the needed output (for example, "From now on, I would like you to ask me questions to..."). |
| 17         | To inquire about a specific topic or idea or any information and you want to test your understanding, you can use the following phrase: “Teach me the [Any theorem/topic/rule name] and include a test at the end, but don’t give me the answers and then tell me if I got the answer right when I respond” |
| 18         | Assign a role to the Language Model (LLM) |
| 19         | Use Delimiters |
| 20         | Repeat a specific word or phrase multiple times within a prompt. |
| 21         | To write an essay/text/paragraph/article or any type of text that should be detailed: “Write a detailed [essay/text/paragraph] for me on [topic] in detail by adding all the information necessary” |
| 22         | To correct/change specific text without changing its style: "Try to revise every paragraph sent by users. You should only improve the user’s grammar and vocabulary and make sure it sounds natural. You should not change the writing style, such as making a formal paragraph casual" |
| 23         | When you have a complex coding prompt that may be in different files: “From now and on whenever you generate code that spans more than one file, generate a [programming language] script that can be run to automatically create the specified files or make changes to existing files to insert the generated code. [your question]." |
| 24         | No need to be polite with LLM so there is no need to add phrases like “please", "if you don't mind", "thank you", "I would like
| 25         | Combine Chain-of-thought (Cot) with few-Shot prompts |
