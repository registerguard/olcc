# os.system("pdftotext '%s' '%s'" % (input1, output))
import os

os.system('pdftotext -table -nopgbrk {0} {1}'.format('resources/liquorlicenseapplications_022717_030217.pdf', 'resources/out_nopagebreak.txt'))
os.system('pdftotext -table {0} {1}'.format('resources/liquorlicenseapplications_022717_030217.pdf', 'resources/out_pagebreak.txt'))
