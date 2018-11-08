#!/bin/sh
rc=0
while read old new refname; do
        if [[ $refname == refs/heads/* && $old != *[^0]* ]]; then
                rc=1
                echo "Refusing to create new branch $refname"
        fi
done
exit $rc