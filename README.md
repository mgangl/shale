# shale

Shale is a python based command line utility which will do environment substitution and configuration based substitution on template files matching the jinja2 templating language. It was made to take yaml configuration and easily generate environment specific compose files for docker deployments.

## Installation

```
git clone https://github.com/mgangl/shale.git
cd shale
pip install .
```

## Usage

Shale requires a configuration file, a stage, and 1..n template files. The files, for now, must end in '.tpl'.

From the samples directory:

```
> shale --config sample.yaml --stage default --file sample.out.tpl
Processing templateFile sample.out.tpl
> cat sample.out
a=default-a
b=default-b
c=default-c
d=d
```

To override the environment variables, simply export the 'VAR_D' variable in your shell:

```
> export VAR_D=default-d

> shale --config sample.yaml --stage default --file sample.out.tpl
Processing templateFile sample.out.tpl

> cat sample.out
a=default-a
b=default-b
c=default-c
d=default-d
```

## Output

The output of a shale run is the template file with appropriate substitutions. The file is written without the .tpl suffix, so something like 'config.cfg.tpl' will become 'config.cfg'.

## The Config File

a sample config file is given in the samples directory. There must be a 'default' stage included. The rest of the stages can be named whatever you'd like, 'dev', 'test', 'uat','prod', etc. Default values apply to all other environments unless overwritten by a specific stage entry.
