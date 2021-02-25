# Lexicon-and-Rule-based-Named-Entity-Recognition
A rule-based named entity recognition system (NER) for Turkish. The NER system identifies followings over a given Turkish text:  
* Person                                                                          
* Location                                                                              
* Organization                                                                          
* Date and Time                                                                                             

Input as following:                                                                     
*Türkiye Cumhuriyeti 1923 yılında kurulmuştur.                                    
İlk cumhurbaşkanı Mustafa Kemal Atatürk'tür.                            
Başkenti Ankara'dır.*                                                     

The NER program gives outputs:

Line 1: ORGANIZATION Türkiye Cumhuriyeti                        
Line 1: TIME 1923                                           
Line 2: PERSON Mustafa Kemal Atatürk                                
Line 3: LOCATION Ankara                                       

There are 5 lexicon scripts                                                          
* Date.py
* Locations.py
* Organizations.py
* Person.py
* Time.py

ner.py is the main script file. The program can be run with following command:                                    
python ner.py input_file > output_file











