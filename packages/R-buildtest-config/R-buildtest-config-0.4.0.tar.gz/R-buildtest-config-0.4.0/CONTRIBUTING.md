# Contributing to R buildtest-config

First off, thank you for your time and effort in making this project a success.
The R buildtest-config repository aims to provide tests for every R package so 
that we can test this with the buildtest framework. If you want to contribute 
back, please create a new issue with the name of the package and a link to the 
tests. Typically most package tests can be found in CRAN but some are not found there. 

For instance if you wanted to create new issue for the **timedate** package, we 
can just update the issue with the link to 
https://cran.r-project.org/web/packages/timeDate/timeDate.pdf where tests can 
be found. Please check the issues to see if the application has 
already been tested to avoid duplicate issues. 

# Writing Tests for R

Writing tests for R is pretty simple, just copy & paste the tests from the
documentation into each file. When creating a file the name should be the 
function that is tested. The CRAN pages have the name for each test following 
by few subsections like **Description, Usage, Format, Author, and Example**. 
Just copy the section under **Example** with the test. Typically you will
have to add the first line in your test **library(<package>)** to load the
library before running test.

Please add a file **reference.txt** with a link to the tests and then commit 
your work. Please create a new pull request when you want to contribute your 
work back.





