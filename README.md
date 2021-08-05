# Simple mail merge utility

This utility can create simple mail merges. Given a template and a CSV with the data, it produces a single output file that can be copied / pasted into individual emails.

`./merge.py template_file data_file output_file`

## Creating the template

This utility uses the Python string template format. While it can take any text file as a template, raw HTML works best. The replacement variables must be valid Python variable names preceded with `$`, e.g. `$first_name`, `$email`, etc.

### Sample template:

```html
<h1>$name</h1>
<h2>$talk_type: $title</h2>

<p><strong>To:</strong><br>
<a href="mailto:$email">$name &lt;$email&gt;</a></p>

<p><strong>Subject:</strong><br>
Confirmation and logistics for your $talk_type at $event</p>

<hr>
<p>Dear $name,</p>

<p>Thank you for presenting a $talk_type at $event. You are confirmed for $date at $time.</p>

<p>The $event program committee</p>

<hr><hr>
```


## Creating the data file

Data is read from a CSV file. The column headings must match the template's variables exactly, excluding the `$`. For example, if a field is called `$first_name` in the template, there must be a CSV column called `first_name`.

### Sample data file:
```csv
name,email,talk_type,title,date,time,event
Brian Warner,bwarner@linuxfoundation.org,lightning talk,How to do a mail merge,August 21st,10:00a EDT,PMO Workshop
Brian Warner,brian@bdwarner.com,workshop,Mail merge walkthrough,August 21st,11:00a EDT,PMO Workshop
```

## Defining the output file

The generator will write a file with all of the merged items in sequence. For best results, output to HTML and include the addressee and subject line so that you can copy/paste them, and include a separator at the end of the template.

Please note you need to use a unique output name; existing files will not be overwritten.
