##################################################################
##                 Perséfone Alpha Test (Prototype)             ##
##            Created by Iván Montalvo and Santiago Buitrago    ##
##################################################################

This is the Repo for the Project Persefone. In here, you will find the parts for running the program,
including the Readme (that you're reading!) and a sample image for testing.

Index:
1. Introduction.
2. Explanation and usage.
3. Other information.
4. Thanks.


Introduction:

  This programs was created for my (Iván) undergraduate theses, which is named "Advances towards the automatic transcription".
  While it sounds ambitious, have in mind that this technology is still in its infancy in the Latin American region, at least
  in the philological field. What this means is the application of neural networks and machine learning in the aforementioned
  area. I know that in many countries this field has been researched, like the TranScriptorium, now READ project in the EU and
  the works of many illustrious professors, such as Tara L. Andrews. Taking the challenge of making a product that unites the
  knowledge of classical philology and the "téchne" of software engineering wasn't easy. I had to ask my childhood friend and 
  colleague Santiago Buitrago for help with the programming. He kindly accepted and took part in this endeavour, teaching me the 
  basics of Python and helping me with the creation of the code. By rule, this makes him co-creator and co-owner of this code, 
  so you, The Reader, may see the same files in another repo. About this I will explain with more depth in the 
  third part of this Readme.
  
  The point of this program is the automatic translation of a colonial book "Physices Tractatus" written by Mateo Mimbela, a
  Catholic Priest from XVI-XVII century. He was a missionary from Spain who did his work in Colonial Colombia. This book is the
  written testimony of his classes as a professor in the Rosary College, one of the oldest (if not the oldest) higher education
  center in the Americas. This work compiles his thoughts about philosophy, physics and theology, following the Sant Thomas 
  Aquinas method for argumentation. The only tome available is located in the National Library of Colombia. This beautiful 
  text is written in a very standardized handwriting, written by one of the students of his class.
  
  One of the most difficult parts in transcribing and reading this text is the amount of abbreviations. Due the time constraints 
  the student faced during the class a lot of often used words are abbreviated, creating a puzzle which image was lost centuries 
  ago and making this transcription process even harder. The abbreviations range from using a different symbol, such as 
  elongated u's or a's; disregarding the vowels in a long letter word and using a special symbol to signifying the missing
  letter, to the point of just missing letters or words without any type of marking. This text becomes arcane even for the
  experts in the philological sciences and working with it demands an amazing amount of patience and knowledge, due the
  complicated topics it delves in. 
 
 There is also the concept of lost knowledge. Many of the books that were written in the colonial times, at least in Colombia,
 were handwritten in latin, for many historical reasons that may not be of importance in this Read me, which didn't allow the 
 flow of information among the common people. Thus, this knowledge must have to be digged through the process of transcription
 and translation. This is one of the main reasons why I created this program. Colombia is a country that needs to learn its own
 history and culture, which is hidden because of political and historical reasons. I will put in the last part some bibliography
 that will support this.
 
 To summarize, Perséfone is a program to transcribe colonial texts to make them easier to translate. This will help to regain
 Colombia's colonial heritage. This program is just a prototype created to be a proof of concept, and with a lot of hard work
 we will update it, creating a user-friendly, powerful tool.
 
 
Explanation and usage:

  This program only runs in a Python environment, for it doesn't have a GUI yet. The recommended modules and libraries are: 
  glob, os, shutil, tkinter, NumPy, OpenCV(version 3.3.0.10), Matplotlib,Sklearn, and PIL. The file to run the program
  is GUI.py, and must use the example image. After selecting four points in the image with a click, which must be 
  the paragraph corners (see image 1). After the processing time, in the folder where the program is allocated you will 
  find the results, an image with the letter character and the top five meaning options. It's important to have the trainData
  folder in the same location the files are, so the program can run correctly.


Other Information:
  
  As stated before, this program is also being worked by Santiago Buitrago, so a lot of new features would be updated first in
  his GitHub, depending on our schedule and who is developing the program. Right now, He is working in different options for
  optimizing the program on his own.
  
  Some of the recommended bibliography, not for the programing but for the historical and cultural context, is in Spanish, and
  while it is possible for it to be in English, I recommend to read them in their original language.
   * Saber, Cultura y Sociedad en el Nuevo Reino de Granada, Siglos XVII y XVIII. Renan Silva (2004)
   * El Latín en Colombia: Bosquejo Histórico del Humanismo Colombiano. José Manuel Rivas Sacconi (1993)
   * Mateo Mimbela (1663-1736), el Maestro Aragonés que Enseñó Filosofía y Teología en el Nuevo Reino de Granada.
   Url:https://www.uco.es/ucopress/ojs/index.php/refime/article/view/9352/8849
   
   It is important to see the full text, especially for those who may find this topic interesting. For this reason, here is the
   link for the digital edition, made by the Pontificia Universidad Javeriana. 
   Url: https://filosofia.javeriana.edu.co/investigacion/grupos-investigacion/bvpfc/publicaciones-bvpfcpc


Thanks:
   
  Thank you to my Advisors, Juan Felipe Gonzalez Calderon and Flavio Augusto Prieto Ortiz. Also the National University of
  Colombia, place of many joys and challenges. Finally, many thanks to Santiago Buitrago, a great colleague and even better
  friend. And to you, The Reader, for checking this project made in three months due the political instability of the country,
  yet as complete as our abilities allowed. 
