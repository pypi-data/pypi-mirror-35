---
title: Using the Tagging Tool
---

This section will walk through the steps for using the tagging tool
application.

Start the Application
=====================

1\. Open a terminal window and navigate to the folder where the tagging
tool is installed. For example, it may be installed in
\'/anaconda3/lib/python3.6/site-packages \' on a Linux machine, but the
installed location might vary from one computer to another and one OS to
another.

2.  Launch the app by typing in \'python ui/app.py\'
3.  The application should open as seen below:

![image6](images/Graphics34_v3.png)

4.  Open your .csv file with your MWOs. Included in the application, is
    a publicly available dataset. We will use this file (mine\_raw.csv)
    as the example.

![image7](images/Graphics35_v3.png)

![image8](images/Graphics36_v3.png)

5.  If you are using the application for the first time, hit "Next"

![image9](images/Graphics37_v3.png)

6.  Select the column(s) that you would like to "tag." In this example,
    the column is "OriginalShorttext." There is also a drop-down to say
    what the column likely represents - this is for the graph based
    representation of the tags later on. The choice made in this example
    is \"issue-description\_problem\". Hit "Next".

![image10](images/Graphics38_v3.png)
![image101](images/Graphics38_v3_2.png)

7.  The application window will open as seen below:

![image11](images/Graphics40_v3.png)

1 Gram Token tab
================

This subsection will describe the features of the application and goes
into detail on the "1 Gram Token" tab.

![image12](images/Graphics41_v3.png)

-   This window contains the following information:
    -   "tokens": The token as seen in the corpus and ranked by TF-IDF
        weighting.
    -   "NE": This is a "Named Entity." This column will track the
        classifications of the tokens, which will be explained in more
        detail later.
    -   "alias": This column tracks any aliases for tokens as made by
        the tool. These represent your new "tags.\"
    -   "notes": This column tracks your notes for any tokens you have
        mapped to an alias.
-   Next, select a token to "tag." In this example, we use "replace."

![image13](images/Graphics42_v3.png)

-   The "similar pattern" field will display words similar to the token
    using an "edit-distance\"-based metric, via
    *[fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)*. Any term
    that is selected here will be given the same alias and
    classification as the original token. So in this example, if
    "replaced" is selected, it will be given the same alias, notes, and
    classification as "replace"

![image14](images/Graphics43_v3.png)

-   The "alias" field will allow a user to enter any alias they would
    like for a token. The field will auto suggest the "token" as-is as
    the initial alias, but the user has the ability to change it to any
    alias they desire.

![image15](images/Graphics44_v3.png)

-   This field is where the user can classify the "token." The
    classifications provided are:
    -   "Item": The objects directly relevant to the issue such as
        machine, resources, parts, etc. An example is a "pump" is always
        an item, however, "pumping" would not be an item.
    -   "Problem": The problem that is occurring at an item. An example
        is "leak" is always a problem.
    -   "Solution": The solution action taken on an item. An example is
        "replace" is always a solution.
    -   "Ambiguous (Unknown)": Words that are unknown without more
        context. An example is "oil" as this can be an item or a
        solution. This is further described in the N Gram Token tab
        section [4.3](#sec:Ngram)
    -   "Stop-word": A word that does not matter for analysis. For
        example, "see" or "according" are stop-words.

![image16](images/Graphics45_v3.png)

-   The "Notes" field allows users to enter notes about the
    token/classifications.

![image17](images/Graphics46_v3.png)

N Gram Token tab {#sec:Ngram}
================

This subsection will describe the features of the application and goes
into detail on the "N Gram Token" tab.

-   The N Gram token tab will provide detail on common 2 grams tokens,
    ordered in TF-IDF ranking, for the corpus (e.g., "hydraulic leak" is
    a common 2 gram in some data sets). The 2 grams can also provide
    more context for the "Uknown" classifications from the above
    section. For example, "oil" is unknown until the user is provided
    more context.

![image18](images/Graphics47_v3.png)

-   When a user selects the N Gram Token tab, the window below is
    presented:

![image19](images/Graphics48_v3.png)

-   The user is presented with the Composition of the 2 gram, which are
    composed of two 1 gram tokens. Each 1 gram is presented, with the
    classification ("type") and the synonyms (the other words that were
    linked with the Similar Pattern subwindow in the above section). In
    this example, "oil" is an "unknown (U)" classification and has no
    other synonyms at this point; "leak" is a "problem (P)" and has no
    other synonyms at this point.

![image20](images/Graphics49_v3.png)

-   There are a number of classifications that a user can select for a 2
    grams. The user will have to classify any 2 grams that contain an
    "U" classification. Please note that some 2 grams will be
    pre-classified based on a ruleset as seen below:

![image21](images/Graphics50_v3.png)

> -   **Problem Item**: This is a problem-item (or item-problem) pair.
>     For example, "hydraulic" is an item and "leak" is a problem so
>     "hydraulic leak" is a problem-item pair. The tool will
>     pre-populate some problem-item pairs using the 1 grams that are
>     classified as problems and items.
> -   **Solution Item**: This is a solution-item (or item-solution)
>     pair. For example, "hydraulic" is an item and "replace" is a
>     solution so "replace hydraulic" is a solution-item pair. The tool
>     will pre-populate some solution-item pairs using the 1 grams that
>     are classified as solutions and items.
> -   **Item**: This is for pairs of items that are de facto 1-grams.
>     For example "grease" is an item, line is an "item", but a
>     "grease\_line" is most likely its own "item\". The tool will
>     pre-populate some items based on 1 grams that are both items.
>     Please note that 2 gram items, since they are really being treated
>     as 1-grams, must have an underscore (\_) in their alias, between
>     the 2 individual items as seen below:

![image22](images/Graphics51_v3.png)

> -   **Problem**: This is a problem that is a 2 gram. This will be left
>     up to the user to classify as these will not be pre-populated
>     using 1 gram classifications. Please note that 2 gram problems,
>     since they are really being treated as 1-grams, must have an
>     underscore (\_) in their alias, between the 2 individual problems.
> -   **Solution**: This is a solution that is a 2 gram. This will be
>     left up to the user to classify as these will not be pre-populated
>     using 1 gram classifications. Please note that 2 gram solutions,
>     since they are really being treated as 1-grams, must have an
>     underscore (\_) in their alias, between the 2 individual
>     solutions.
> -   **Ambigious (Unknown)**: This is an unknown 2 gram that needs more
>     context. This will be left up to the user to classify as these
>     will not be pre-populated using 1 gram classifications.
> -   **Stop-word**: This is 2 gram stop-word. This will be
>     pre-populated when a "solution" 1 gram is paired with a "problem"
>     ' gram. The user can decide if any other 2 grams are not useful.

Report tab
==========

Once the user is done tagging their desired amount of tokens, they can
begin using the report tab.

-   Please make sure to hit the "update tag extraction" button before
    proceeding. This may take some time to compute.

![image23](images/Graphics52_v3.png)

-   The bottom graph will update. It explains the amount of tagging that
    has been completed. The distribution of documents (shown as a
    histogram) is calculated over the precision for each document (i.e.
    of the tokens found in a document, what fraction have a valid
    classification defined).

![image24](images/Graphics53_v3.png)

-   Summary statistics are also shown.

![image25](images/Graphics54_v3.png)

-   The "create new CSV" button will create an .csv with the original
    dataset and 7 new columns ("I","P","PI", "S","SI","U", and "X") ,
    which contain the new tags from each category. Please note that "X"
    contains any stop words.

![image26](images/Graphics55_v3.png)

-   The "create a binary CSV" button will create 2 new .csv files. Each
    file will contain the work order number (starting with 0), and is
    ordered identically to the .csv file that was originally loaded. Two
    new files are created: binary\_tags and binary\_relations.

![image27](images/Graphics56_v3.png)

> -   **binary\_tags**: The left most column contains the work order
>     number, while the headers contain all 1 gram tags. A "0" is placed
>     when the work order does not contain the tag in the header and a
>     "1" is placed when the tag in the header is contained in the work
>     order.
> -   **binary\_relations**: The left most column contains the work
>     order number, while the headers contain Problem-Item and
>     Solution-Item tag combinations. A "0" is placed when the work
>     order does not contain the tag in the header and a "1" is placed
>     when the tag in the header is contained in the work order.
