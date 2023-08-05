import unittest
from collatex import *


class Test(unittest.TestCase):
    def test_export_alignment_table_as_tei(self):
        output_expected = """<?xml version="1.0" ?><cx:apparatus xmlns="http://www.tei-c.org/ns/1.0" xmlns:cx="http://interedition.eu/collatex/ns/1.0">The <app><rdg wit="#A">quick</rdg></app> brown <app><rdg wit="#A">wombat</rdg><rdg wit="#B #C">koala</rdg></app> jumps over the <app><rdg wit="#A #C">industrious</rdg><rdg wit="#B">lazy</rdg></app> <app><rdg wit="#A">brown</rdg><rdg wit="#B #C">yellow</rdg></app> dog.</cx:apparatus>"""
        collation = Collation()
        collation.add_plain_witness("A", "The quick brown wombat jumps over the industrious brown dog.")
        collation.add_plain_witness("B", "The brown koala jumps over the lazy yellow dog.")
        collation.add_plain_witness("C", "The brown koala jumps over the industrious yellow dog.")
        output = collate(collation, output="tei")
        self.assertEqual(output_expected, output)

    def test_export_alignment_table_as_tei_prettyprint(self):
        output_expected = """<?xml version="1.0" ?>
<cx:apparatus xmlns="http://www.tei-c.org/ns/1.0" xmlns:cx="http://interedition.eu/collatex/ns/1.0">
	The 
	<app>
		<rdg wit="#A">quick</rdg>
	</app>
	 
	brown 
	<app>
		<rdg wit="#A">wombat</rdg>
		<rdg wit="#B #C">koala</rdg>
	</app>
	 
	jumps over the 
	<app>
		<rdg wit="#A #C">industrious</rdg>
		<rdg wit="#B">lazy</rdg>
	</app>
	 
	<app>
		<rdg wit="#A">brown</rdg>
		<rdg wit="#B #C">yellow</rdg>
	</app>
	 
	dog.
</cx:apparatus>
"""
        collation = Collation()
        collation.add_plain_witness("A", "The quick brown wombat jumps over the industrious brown dog.")
        collation.add_plain_witness("B", "The brown koala jumps over the lazy yellow dog.")
        collation.add_plain_witness("C", "The brown koala jumps over the industrious yellow dog.")
        output = collate(collation, output="tei", indent=True)
        self.assertEqual(output_expected, output)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSuffix']
    unittest.main()