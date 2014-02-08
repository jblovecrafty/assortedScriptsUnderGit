#!usr/bin/perl;

use strict;


#set up vars
my $passedFileName = @ARGV[0];
my $passedSearchFileName = @ARGV[1];
my $passedEndFileName  = @ARGV[2];
my $delimiter = "|";
my $isIn = 0;

my $passedReadingLine;
my @passedReadingLineArray;
my $passedSearchLine;
my @passedSearchArray;
my $searchFinalLine;

#open passed in file
open PASSINGFILE, "<", $passedFileName or die $!;
open SEARCHINGFILE, "<", $passedSearchFileName or die $!;
open ENDFILE, ">", $passedEndFileName or die $!;

while(<SEARCHINGFILE>)
{
	$passedSearchLine = "";
	$passedSearchLine = $_;
	chomp($passedSearchLine);
	
	print $passedSearchLine;
	
	push(@passedSearchArray, $passedSearchLine);
}


while(<PASSINGFILE>)
{
	$passedReadingLine = "";
	$passedReadingLine = $_;
	chomp($passedReadingLine);
	
	@passedReadingLineArray = split(/\Q$delimiter/, $passedReadingLine);
	
	foreach $searchFinalLine (@passedSearchArray)
	{		
	    if(lc($passedReadingLineArray[0]) eq lc($searchFinalLine))
		{
			print ENDFILE $passedReadingLine."\n";
		}
	} 
	
	@passedReadingLineArray = {};
}

close PASSINGFILE;
close SEARCHINGFILE;
close ENDFILE;