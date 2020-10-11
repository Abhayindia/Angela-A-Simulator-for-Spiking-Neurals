#!/bin/bash

pylint --rcfile=dev/jenkins/pylint.rc angela2 > pylint.log || :
