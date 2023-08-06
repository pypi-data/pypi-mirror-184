### clise: Command Line Input Sender

Command liner for python routines using JSON based input parameter files. 
It dives into a module with CLI and execute a routine just as herons dive into
water and catch fish. Rabbits enable JSON text to automatize multiple
executions of the routine: ver 0.0.3 by Jaesub Hong (jhong@cfa.harvard.edu)

       Usage:  JSON_input_file1 -options_for_file1 ... \
            [json_input_file2 -options_for_file2 ...] \
            [--with common_json_files -common_options ...]

       --help 
       [json_files ...] --Help 
       --main module.routine --Help 

### Table of Contents
- [Quick overview of the basic concept](#quick-overview-of-the-basic-concept)
- [Installation and startup](#installation-and-startup)
- [Features and limitation](#features-and-limitation)
- [Features in parameter setting with JSON files](#features-in-parameter-setting-with-json-files)
- [Iterative calling and file search](#iterative-calling-and-file-search)
- [Sequential calling](#sequential-calling)
- [Options for command line parameters](#options-for-command-line-parameters)
- [Parameter list](#parameter-list)
- [Logging](#logging)
- [Changes](#changes)

### Quick overview of the basic concept

There are many command line interface tools for python (e.g., pyCLI). They
usually provide decorators and other useful functions to deal with arguments.
They also provide routines to generate the executable scripts for the user
functions. While these are great for developing a large code or project, it can
be a bit redundant for a quick test of a function in a code you don't have
access to modify. In these cases, you may have to write your own wrapper to
bypass that. CLISe takes a different approach.

CLISe enables executions of any function as a command script only with input
parameters either in a command line or with an input file (in c-style
commentable JSON format). CLISe dynamically make a decorator for the called
function, handling the input and output parameters of the function, so the user
doesn't need to modify the original function. One of the input parameters
required for CLISe is the function and module name itself. So when the input
parameter is stored in a file (recommended), the user doesn't need to remember
the function name in future runs. For more complex operations, CLISe allows a
sequential call of multiple functions, and provide a simple mechanics to
generate multiple calls of multiple functions.

The input parameter files can contain the name of the routine to call:
e.g., "-main": "module.routine".  Keys starting with alphabets are assumed to be
fed into the main routine set by "-main" key.  Assume that a python script
example.py has

      def my_sum(name, x, y):
           """ This is my sum. """
           print(name+':', x+y)

Then with a JSON file input.json,

      "-main": "example.my_sum",
          "x": 5,
          "y": 7,
       "name": "answer",

one can execute the routine 'my_sum' in a shell command prompt like

      % clise input.json
      answer: 12

In principle, all the content in the JSON files can be fed as a long string in
the command line or as optional parameters for individual keys with "-". So the
above example is equivalent to the followings even without the JSON file
input.json.

      %  clise --main example.my_sum -#x 5 -#y 7 -name "answer"
      %  clise '{"-main":"example.my_sum","x":5,"y":7,"name":"answer"}'

or some combination of all three examples:

      %  clise '{"-main":"example.my_sum","name":"answer"}' -#x 5 -#y 7
      %  clise input.json '{"name":"answer"}' -#x 5 -#y 7

When both JSON files and command line input options are available for the same
key, the command line options take a priority.  Note # in -#x ensures it is a
number but not a string.  See more details with 'clise --help cmdline'. Note --Help
(capital H) prints out the doc string of the routine.

      % clise input.json --Help
      This is my sum.

Calling multiple JSON files execute them in sequence.

      % clise input.json input.json
      answer: 12
      answer: 12

      % clise input.json -#x 7 input.json -#x 6
      answer: 14
      answer: 13

As you may have guessed it by now, in the comand line, "--" is reserved for
options for clise itself, and "-" is reserved for options and keys of the
called function. In JSON files, the parameters lose one "-", so "-var" are 
for the clise, and "var" without "-" is for the called function.

Find out what kind of parameters are needed to call the routine using --show
func option.

      % clise --main os.path.isfile --show func
       main: os.path.isfile
       path

The above example shows isfile expect a parameter called path.

      % clise --main os.path.isfile -path clise.py --show output
      True

Can check how the parameters get fed to the routine.

      % clise --main os.path.isfile -path clise.py --show feed
       main: os.path.isfile
       path << str .py

      % clise input.json --show feed
       main: example.my_sum
       name << str answer
          x << int 5
          y << int 7

Can call a routine needing no input parameters.

      % clise --main datetime.datetime.now --show output
      2022-04-27 22:11:52.983532

One can force the parameters to a function with --pars option.

      % clise --main math.sin --pars x --show output -#x 1.0
      0.8414709848078965

In the case of the built-in functions: e.g.,

      % clise --main eval --pars x --show output -x 3+3
      6

      % clise --main pow -*-pars x,y --show output -#x 1.5 -#y 3
      3.375

      % clise --main eval --pars x --show output -x 'pow(1.5,3)'
      3.375

### Installation and startup

Install the  package using pip,

      % pip install 

then assign an alias for easy use: e.g., in bash,

      % alias ="python -m clise"

Alternatively, this program can be used without installation: simply
place clise.py in the python path and use

      % alias ="python clise.py"

For a common parameter configuration, assign an environmental variable
CLISE_STARTUP to a JSON file with the common parameters: e.g.,
in bash,

      % export CLISE_STARTUP="~/my_startup.json"

The parameters in this file will be loaded as well.

By default,  will attempt to pass parameters starting only with alphabets
to the routine in call, but one can accept the full parameter sets
(including -main) by adding an optional parameter named _heron_ in your function:

      def my_routine(..., _heron_, ...):
            ...

One can change the name of the parameter to something else by "-roundup".
(i.e., by default, "-roundup": "_heron_").

then, all the input parameters (both from JSON files and CLI) will be passed to
this parameter as collections.OrderedDict. This may be useful for debugging.

One can also use  inside python or ipython for a single task: e.g.,

      >>> from clise import heron, rabbit, jsontool
      >>> cfg = jsontool.load_cli('command line input string')
      >>> out = heron.go(*cfg)

### Features and limitation

There are many excellent packages that handle input parameters of
routines and link them to matching command line tools. The main purpose
of this program is, though, to facilitate a command line call of an arbitrary
python routine without additional wrapper script for the routine. At
the same time, for some tasks, the input parameters themselves are part
of the important data to keep and track.  CLISe encourages the use
of an input file in JSON format for input parameters, so that the input
parameters are available for later review, modification and rerun.  Since
the input parameters contain the name of the main routine to call (i.e.,
poor man's objective oriented programming), there is no need for
additional wrapper script.  For simple routines that don't really need
the input parameter files, a simple alias can be used for easy repetitive
call instead of a wrapper script (try --help startup). Some of
the main features are:

- Calling a python routine from a command line without any wrappers
- Enable somewhat a clean separation between the routine (program) and
  the input parameters (data).
- Support iterative routine calling with minimal parameter setting
- Support calling multiple routines sequentially
- Provide flexible command line options for easy on-the-fly modification
  of parameter changes
- Support automatic logging of the input parameters and run condition
  through hashing
- Support rudimentary extension of JSON format including commenting,
  simple math, and variable substitution.
- Provide recursive file search function with basic regex for the cases
  that the same routine has to deal with lots of similar-type but
  different files.
- Provide the check of the mod time of files to process and enable an
  easy option to what to process and what not to process.
- Allow an option to pass the complete set of the input parameters for
  routines that are written specifically for 
- When the called routine returns another routine, the new routine is
  also called.

In regarding the data type of input parameters,  provides a few tools
to ensure proper types, but not as strict as some of other tools. The motto is
"quickish and dirtish" is good enough, although we don't want to go as far as
"quick and dirty.

The current limitations of the program are:
- Type checking of the parameters: since CLISe doesn't impose any changes in
  the original functions, it doesn't provide a solid way to type check input
  parameters. However, one can use '--enforce_format' to set the type
  explicitly. In addition, '#', '##','\*','\*#', and '\*\*' can be used to
  specify the data type in the command line and JSON files: e.g., in a command
  line, '-x 1' means "x" is a string of "1", while '-#x 1' means "x" is an
  integer of 1.

- Routines of a class: this should work in principle and it does under a
  limited circumstances. For instance, the 2nd-to-last item of the -main
  parameter can be a class name. If so, the class will be initialized.
  e.g., with "-main": "plottool.plottool.collect_data",  will
  initialize the class "plottool" of the module "plottool" with an object
  and call the function "collect_data" under the same object.  If
  a following routine is "plottool.plottool.mplot1d", then CLISe will call the
  function "mplot1d" under the same object of the class. In this way, one
  can pass parameters among multiple functions through the class
  definition, requiring no additional parameter settings in the JSON input file.

- Routines with decorators or processed by function manipulators often end up
  with unclear arguments and keyword arguments when called from the outside,
  sometimes split over the original routine and decorators/manipulators.  In
  this case, the user has to manually make sure what parameters are fed (in
  what order for non-keyword parameters). Use -collect_kwpars and -discard to
  efficiently facilitate this.

### Features in parameter setting with JSON files

In, the JSON format is used for input parameter files. There may be other
more popular or capable formats, but JSON seems to be one of the most compatible
formats with the python dictionary, which is versatile and easy to handle, even
though it tends to be a bit verbose.

Unlike the standard JSON, commenting is allowed in  with the c-style
notation of //. The outermost "{" and "}" can be omitted to simulate a more
configuration-file like feel. String-only variables are allowed for tagging &
replacing by calling the "key" in the "{key}" format: e.g.,

      "key1": "Abcdef", "key2": "{key1} & more" is equivalent to
      "key1": "Abcdef", "key2": "Abcdef & more"

Enclosures "{>" and "}" allow a similar subsititution, but the substitution
occurs after all other variables are substituted.

      "k1": "Abcd", "k2": "{k1}!", "k3": "{k2}?" is equivalent to
      "k1": "Abcd", "k2": "Abcd!", "k3": "{k1}!?"

      "k1": "Abcd", "k2": "{k1}!", "k3": "{>k2}?" is equivalent to
      "k1": "Abcd", "k2": "Abcd!", "k3": "Abcd!?"

For non-string variables, use {= and }: e.g.,

      "key1": [1.5, 20], "key2": "{=key1}"  is equivalent to
      "key1": [1.5, 20], "key2": [1.5, 20]

Basic math expressions in <expr> are allowed: e.g.,

      "key" : <3+4*5> changes to "key": 23.

Trailing commas are allowed: e.g.,

      "key": [1,2,3,] is the same as "key": [1,2,3].

The built-in keys like infile can be used with wild cards, which automatically
generate a matching file list and successively call the main routine with each
file.  {1}, {2}, ... {key:1}, {key:2}, ... are reserved for tagging and
replacing by regex in infile and other parameters for iterations: e.g.,

      "infile": "(.*)([0-9]+).txt", "outfile": "{1}__{2}.txt"

If the infile parameter encounters files named hello3000.txt, hiThere2000.txt
..., the main routine will be iteratively called with

      "infile": "hello3000.txt",   "outfile": "hello__3000.txt"
      "infile": "hiThere2000.txt", "outfile": "hiThere__2000.txt"
     ...

These features are desirable for convenience, but semi-intentionally limited in
order to keep JSON file mainly for input parameters without over-stepping into
the programming side.  Given the rather relaxed rules for JSON in ,
recommend avoiding multi-line parameters, which can conflict with commenting and
others. Nested variables (dictionary or hash) are ok to use.

Parameters with ==, ~=, != in their keys can be used for a pattern matching to
make exceptions through built-in  functions like combine_tags: e.g.,

      e.g., "infile~=.txt$" : { "x-value": 90, ... }.

What this can do is that when the parameter infile meet files ending with
".txt", x-value is set to 90, superceding other possible settings for x-value.

### Iterative calling and file search

A single input JSON file can set up an iterative call to a function.
Going back to the example example.my_sum (try --help
overview), now we have a new JSON file called iterations.json:

      "-main": "example.my_sum",
      "x": 5,
      "y": 7,
      "name": "answer",

      "-id": ["run A", "run B", "test C"],

      "run A" : { "x": 1,  "y": 2,  },
      "run B" : { "x": 10, "y": 20, },
      "test C": { "x": 10, },

      "-id~=run": { "name": "ANSWER", },

This example will run three cases in sequence as specified in [tt} iter.

      % clise iterations.json
      ANSWER: 3
      ANSWER: 30
      answer: 17

The key -id is reserved for setting an ID for each run when it is a string.
When it is a list of strings, it indicates an iteration. The parameters in the
outside or top level will be default, and for each case, when a new value is
given, the default value will be substituted. CLISe will look for parameter names in
the list -id, and substitute variables inside.  Note "-id~=run" allows the
variable substitution for any tasks whose name contains "run". Three such
expressions are allowed for key matching:

      "-id~=run"  for any keys containing "run"
      "-id==run"  for key which is "run"
      "-id~!=run" for any keys not containing "run"
      "-id!=run"  for any keys which are not "run"

To see the progress with runs:

      % CLISe iterations.json --show job
      # of jobs: 3
      job 1/3: example.my_sum run A
      ANSWER: 3
      job 2/3: example.my_sum run B
      ANSWER: 30
      job 3/3: example.my_sum test C
      answer: 17

The "-infile.key==#" is reserved for setting options for selected infile
parameter, useful when the same file is used more than once. # indicates the
index of the "infile" parameter.

      "infile" : ["(.*).py","(.*).py","(.*).sh"],
          ...
            "-infile.key==0" : { "x":1, "y":2 },
            "-infile.key==1" : { "x":2, "y":3 },
            "-infile.key==2" : { "x":3, "y":0 },

The files named "*.py" will have two runs each: first with input
parameters being x=1 & y=2 and the 2nd run with x=2 & y=3.
The files named "*.sh" will have a single run with x=3 & y=0.
One can also mark a certain files with " >?", where ? is a non-numeric
character.

      "infile" : ["(.*).py","(.*).py >a","(.*).sh"],
          ...
            "-infile.key==0" : { "x":1, "y":2 },
            "-infile.key==a" : { "x":2, "y":3 },
            "-infile.key==2" : { "x":3, "y":0 },

In this example, the 2nd run with files named "*.py" is labeled "a",
whose parameters can be set with "-infile.key==a".

Since input JSON files shouldn't be the place for programming, there is
no features of loop using "for", "while", or "range", etc. However, when a
main input is a file (key infile), a more flexible features are
available based on matching file parameters (name, mod time, and file size).

Now imagine a 2nd routine in example.py":

      def show_new_name(infile, outfile):
      """ Come up with a new file name"""
      print(infile, ">>", outfile)

which simply prints out two parameters. With onefile.json:

      "-main": "example.show_new_name",
      "infile" : "input.json",
      "outfile": "input_json.txt",

Then,

      % clise onefile.json
      input.json >> input_json.txt

Now with manyfiles.json:

      "-main": "example.show_new_name",
      "infile" : "(.*).(json)",
      "outfile": "{1}_{2}.txt",

Then,
      % clise manyfiles.json
      input.json >> output.txt
      iterations.json >> iterations_json.txt
      manyfiles.json >> manyfiles_json.txt
      onefile.json >> onefile_json.txt

The same can be achieved directly in the command line.

      % clise --main example.show_new_name \
            -infile '(.*).(json)' -outfile '{1}_{2}.txt'

The key infile is reserved for simple regex based file search
and followup iteration. The regex can be captured with tags {1}, {2}, ...
and used for other keys like outfile in this example.  Since
both infile and outfile keys are regular variables, we expect
the routine in call to receive them.

The regex for  is somewhat limited. All the capturable text
and regex should be in ( and ). The expression of '(.*).(json)'
will be equivalent to a file search with *.json.

In addition to regex, keys such as -include, -exclude, -keep, -drop,
-after, -before, -larger & -smaller are reserved for further screening: e.g.,

      % clise manyfiles.json -after iterations.json --timekey infile --^parse
      manyfiles.json >> manyfiles_json.txt
      onefile.json >> onefile_json.txt

This only works on the input files modified after iterations.json was
last modified.  The key --timekey in the command  line is
needed to set key -after is applied to infile in the
JSON file (by default it applies to outfile, but we don't
generate any actual outfile in this example).  The key {tt}
--^parse is needed since  will try to attempt to parse any
*.json files instead of using it as parameters.

For more complex screening and the tasks needed after iteractions, use
keys -prep & -post. Try --help decoration.

### Sequential calling

Multiple jobs can be executed in sequence by simply listing them: e.g.,

      %  job1.json job2.json ...

By default, they get executed independently, so this is equivalent to

      %  job1.json
      %  job2.json
      ...

The output of the one job in the first example can be fed to the input
of the next job. This feature hasn't been tested extensively.

      %  job1.json -par "a" job2.json -par "b" ...

Note in this example, par is set to "a" for job1.json and "b"
for job2.json

      %  job1.json -par "a" -par "b"

In this example, par is simply set to be "b".

      %  job1.json job2.json --with job3.json

In this example, each job is first combined with job3.json and executed, which
is equivalent to:

      %  job1.json --load job3.json
      %  job2.json --load job3.json

### Options for command line parameters

All the parameters can be used either in a JSON file or as a command line
option: e.g., {"infile":"filename"} in the JSON file is equivalent to
-infile filename in the command line.  The full content in JSON
can be used in the command line through JSON syntax albeit complex: e.g.,
'{"key":value,... }'.

There is no automatic type checking, but a few options to enforce numeric or
list are available.  See below.  When there are multiple instances of a same
key, the last assignment is used except when it is given after --with
parameter: the command line option of the same parameter is used over the same
of the JSON file.

- Keys without any value mean a boolean variable: e.g.,

        -key in command line is equivalent to {"key": true} in JSON
       -^key is equivalent to { "key": false}
      --^key is equivalent to {"-key": false}
      -^-key is equivalent to {"-key": false}

- Keys starting with # and ## will be enforced
  as numbers and floats, respectively: e.g.,

        -key 1   is equivalent to {"key": "1"}
       -#key 1   is equivalent to {"key": 1}
       -#key 1.0 is equivalent to {"key": 1.0}
      -##key 1   is equivalent to {"key": 1.0}

  Use "-enforce_format" key in JSON files which enables formatting without
  prefix: e.g., in a JSON file,

      "-enforce_format" : {
              "x" : "float",
              "y" : "complex",
              ...
            }

  Then, the command line option -x 1 will keep x as a float instead of str.


- Keys starting with * will be treated as list: e.g.,

         -key 5,Ab,6.1 is equivalent to {"key": "5,Ab,6.1"}
        -*key 5,Ab,6.1 is equivalent to {"key": ["5","Ab","6.1"]}
       -*#key 5,Ab,6.1 is equivalent to {"key": [5,"Ab",6.1]}
      -*##key 5,Ab,6.1 is equivalent to {"key": [5.0,"Ab",6.1]}

- Keys starting with : will be treated as a nested dict: e.g.,

      -key1:key2 abc is equivalent to {"key1": {"key2":"abc"}}

Several handy command line options are:

      --Help  bool false    display the doc text of the user routine

      --help  bool false    display the main section of the help string
              str  overview describe the concept and overview
                   JSON     illustrate features of parameters set in JSON files
                   pars     list parameters used in 
                   cmdline  display features of command line options
                   all      display all the help text

      --show  bool false    show information about the parameters and jobs
              list        * indicates exit without calling the routine
                   hidden * show also the hidden variables
                   func   * expected function's parameter
                   input  * parameters prepared
                   feed   * how the parameters are fed to the function
                   output   output of the function
                   job      job progress
                   files    input and output file status
                   time     time
             e.g., --show          shows the basic input parameters and exit
                   --show job,time shows both the job prgress and run time

      --raw   bool false show the input parameters in the standard JSON format
      --with  list None  JSON input files used with all other JSON input files.
      --relay bool false when multiple routines are called, their data can be
                              sequentially passed.
      --parse bool true  parse *.json files instead of treating them as
                              parameter values.

### Parameter list:

For command line parameters, add the additional prefix -:i.e., "-main" in a JSON
file is equivalent to --main as a command line option.  Parameters starting with
alphabets can be potentially fed into the routine called.

      -main       str  None   the main module and routine to call
      -load       str* None   load other JSON file: same as --with option in the
                              command line
      -loop       str* or dict None   task list for looping or function to
                              define the task list
      -id         str  auto/manual   short term ID for the run
                              auto: routine name
                              manual: set by a user for loop. See multiiply_manual_by_id
      -nid        int  auto   number ID for the run
      -fid        str  auto   full ID for the run
      -rabbit

      -include    str  None   only choose input files with matching string:
                              regex
      -exclude    str  None   do not choose input files with matching string:
                              regex
      -after      str  None   run only for outfile (default) modified after this
                              time
      -before     str  None   run only for outfile (default) modified before
                              this time
      -clobber    bool false  overwrite the existing results

      -hisfile    str  none   copy of input JSON file and command line option,
                              automatically generated if set to be "_auto_".
      -logfile    str  none   log file
      -save_cmdline_log bool false save log for cmdline tools

      -repeat     str  none   will the call be made repeatly? variable,
                              filename, ""
      -native     str  none   is the function  native or generic?

      -global     str* none   global variables
      -pars       str* none   input parameters of the function called; must set
                              this for invisible non-keyword parameters: e.g.,
                              decorated functions
      -kwpars     str* none   input keyword parameters of the function called;
                              set this for invisible keywords or simply set
                              -collect_kwpars true
      -collect_kwpars bool false set this true to feed all the unassigned
                              parameters starting with alphabets as keyword
                              paramters when the routine's keyword parameters
                              are not visible. Use --show feed to check how the
                              parameters are passed.
      -discard    str* none   discard these parameters before calling the routine
      -nonify     str* none   set these parameters None and feed to the routine

      -init      bool or dict true  initialize class or define class parameters

      -inherit   bool true for regular match, false for key match inherit parent
                              parameters for the matching case

      -enforce_numeric str #  a prefix to specify cmdline par being a number
                              instead of string; "" to disable it
      -enforce_floats str ##  a prefix to specify cmdline par being a float
                              instead of string; "" to disable it
      -enforce_format  dict none  a full dict for data format enforcer, int,
                              float, complex, bool, str
      -expand_nested   str ,  a separator to indicate the nested key or
                              parameter; "" to disable it

      -dict_pre     str  **    a prefix to indicate a list in string variable; ""
                              to disable it
      -list_pre     str  *    a prefix to indicate a list in string variable; ""
                              to disable it
      -list_sep     str  ,    a separator to indicate a list in string variable;
                              "" to disable it
      -pop_modifier bool true remove the modifier keys like -enforce_numeric afterwards

      -only for module.routine dict none settings that only apply to a
                              particular module.routine

rabbit.multiiply_manual_by_id
      -id


rabbit.multiiply_auto_by_file

      infile     str* None   regex of input files, any regex should be in (),
                              which can be tagged as {1}, {2},...
      outfile    str  None   output file, one can use tags in input file

      indir      str  None   input directory root, needed for recursive search,
                              otherwise optional
      outdir     str  None   output directory root, needed for recursive output
                              matching input, otherwise optional
      outsubdir  str  None   when an additional subdirectory name is needed to
                              be added
      mkoutdir   bool true   make output dir if not exists

      sort       str  None   Sort by name, basename, modtime, or size. The
                              default changes to modtime if -after/-before is
                              set, or to size if -larger/-smaller is set.

      -verbose    int  1      chatter level

      recursive  bool true   recursive input file search, requires indir
      mirror     bool true   when input files are searched recursively, does
                              output follow the same directory structure?
                              required outdir
      swapsub    dict None   when mirroring indir, if certain subdirectory
                              names needed to be changed
      infile_order  str sort reverse, unsort: sort input files? (obsolete: use
                              -sort)

      tagkeys    str* None   list of file parameters to grab tags
      appkeys    str* None   list of parameters to apply tags

      -timekey    str  -outfile file key to apply time cut with after and
                              before.
      -sizekey    str  -outfile file key to apply size cut with larger and
                              smaller
      -sortkey    str  -infile  file key to sort with -sort

### Logging 

The automatic logging of each run and a copy of the input parameters are
enabled through -logfile and -hisfile = "_auto_".
The log file contains the SHA1 has result of the input parameters, so
that one can tell the same run has been run or not.

22-04-28 11:27:58 0:00:00.000100 \
SHA1:81e37f0fee49f9729aaebe684e9853544664972b example.show_new_name  meco

When some of the routines are used frequently as a command line tool
instead of tasks, the logging and copying can be disabled. In general,
key --^parse sets the auto log off, which can be set by key
-save_cmdline_log.


### Changes

v0.0.2 2023/01
      - Initial version
      - Forked from cjpy
      - Implement sequential run with JSON blocks {}
      - Implement custom routine for iterative calls
