##################################################################
##                 Perséfone Alpha Test (Prototype)             ##
##            Created by Iván Montalvo and Santiago Buitrago    ##
##################################################################

This is the Repository for the Project Perséfone. In here, you will find the parts for running the program,
including the Readme (that you're reading!), a sample image for testing, the training bank and a result sample.

Index:
1. Introduction.
2. Explanation and usage.
3. Other information.
4. Thanks.


# Introduction:

  This programs was created for my (Iván) undergraduate thesis, which is named "Advances towards the automatic transcription".
  While it sounds ambitious, have in mind that this technology is still in its infancy in the Latin American region, at least
  in the philological field. What this means is the application of neural networks and machine learning in the aforementioned
  area. I know that in many countries this field has been researched, like the TranScriptorium, now READ project, in the EU and
  the works of many illustrious professors, such as Tara L. Andrews. Taking the challenge of making a product that unites the
  knowledge of classical philology and the "téchne" of software engineering wasn't easy. I had to ask my childhood friend and 
  colleague Santiago Buitrago for help with the programming. He kindly accepted and took part in this endeavour, teaching me the 
  basics of Python and helping me with the creation of the code. By rule, this makes him co-creator and co-owner of this code, 
  so you, The reader, may see the same files in another repo. About this I will explain this in more depth in the 
  third part of this Readme.
  
  The point of this program is the automatic transcription of a colonial book "Physices Tractatus" written by Mateo Mimbela, a
  Catholic Priest from XVII-XVIII century. He was a missionary from Spain who did his work in Colonial Colombia. This book is 
  the written testimony of his classes as a professor in the Rosary College, one of the oldest (if not the oldest) higher 
  education center in the Americas. This work compiles his thoughts about philosophy, physics and theology, following the Saint 
  Thomas Aquinas method for argumentation. The only tome available is located in the National Library of Colombia. This 
  beautiful text is written in a very standardized handwriting by Juan de Herrera, one of the students of Mimbela's class.
  
  One of the most difficult parts in transcribing and reading this text is the amount of abbreviations. Due the time constraints 
  the student faced during the class, many frequently-used words are abbreviated, creating a puzzle for which the key 
  was lost centuries ago and making this transcription process more difficult. The abbreviations range from using a different 
  symbol, such as elongated u's or a's; disregarding the vowels in a long letter word and using a special symbol to signifying 
  the missing letter, to the point of just missing letters or words without any type of marking. This text becomes arcane even 
  for the experts in the philological sciences and working with it demands an amazing amount of patience and knowledge, due the
  complicated topics it delves in. 
 
 There is also the concept of lost knowledge. Many of the books that were written in the colonial times, at least in Colombia,
 were handwritten in latin, for many historical reasons that may not be of importance in this Readme, which didn't allow the 
 flow of information among the common people. Thus, this knowledge must have to be dug through the process of transcription
 and translation. For various historical and political reasons, colonial Colombia history is not well-known. This is one of the 
 main reasons why We created this program. Please find sources supporting this statement at the end of the document
 
 To summarize, Perséfone is a program to transcribe colonial texts to make them easier to translate. This will help to regain
 Colombia's colonial heritage. This program is a prototype created to be a proof of concept. This intent is to update it, 
 creating a powerful, user-friendly tool.
 
 
# Explanation and usage:

  This program only runs in a Python environment, for it doesn't have a GUI yet. The recommended modules and libraries are 
  glob, os, shutil, tkinter, NumPy, OpenCV(version 3.3.0.10 with the cv2_contrib), Matplotlib,Sklearn, and PIL. The file to run 
  the program is GUI.py and must use the example image (rm_149_021). After selecting four points in the image with a click, 
  which must be the paragraph corners (see image 1). After the processing time, in the folder where 
  the program is allocated you will find the results, an image with the letter character and the top five meaning options. 
  It's important to have the trainData folder in the same location as the files, so the program can run correctly.


# Other Information:
  
  As stated before, this program is also being worked on Santiago Buitrago, so any new features would be updated first in
  his GitHub, depending on our schedule and who is currently developing the program. Right now, He is working on different 
  options for optimizing the program on his own.
  
  Some of the recommended bibliography, not for the programing but for the historical and cultural context, is in Spanish, and
  while it is possible for it to be in English, it is preferable for them to be read in their original language.
  
   * Saber, Cultura y Sociedad en el Nuevo Reino de Granada, Siglos XVII y XVIII. Renan Silva (2004)
   * El Latín en Colombia: Bosquejo Histórico del Humanismo Colombiano. José Manuel Rivas Sacconi (1993)
   * Mateo Mimbela (1663-1736), el Maestro Aragonés que Enseñó Filosofía y Teología en el Nuevo Reino de Granada.
   Url:https://www.uco.es/ucopress/ojs/index.php/refime/article/view/9352/8849
   
   It is important to see the full text, especially for those who may find this topic interesting. For this reason, here is the
   link for the digital edition, made by the Pontificia Universidad Javeriana. 
   Url: https://filosofia.javeriana.edu.co/investigacion/grupos-investigacion/bvpfc/publicaciones-bvpfcpc


# Thanks:
   
  Thank you to my Advisors, Juan Felipe Gonzalez Calderon and Flavio Augusto Prieto Ortiz. Also the National University of
  Colombia, place of many joys and challenges. Finally, many thanks to Santiago Buitrago, a great colleague and even better
  friend. And to you, the reader, for your interest in this project, which was made in just three months due to the political 
  instability of Colombia, yet as complete as our abilities allowed. 
