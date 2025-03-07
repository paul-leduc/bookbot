from stats import get_book_text
from stats import word_count
from stats import char_distribution
from stats import sort_on, dict_to_list
from stats import report
import sys

def main():

	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>") 
		sys.exit(1)
	
	fp=sys.argv[1]
	report(fp)
	
main()

