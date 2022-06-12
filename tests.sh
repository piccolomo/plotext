plotext scatter --path test --xcolumn 1 --ycolumns 2 --lines 5000 --title "Scatter Plot Test"

read -p ""
plotext plot --path test --xcolumn 1 --ycolumns 2 --sleep 0.1 --lines 230 --clear_terminal True --color magenta+ --title "Plot Test"

read -p ""
plotext plot --path test --xcolumn 1 --ycolumns 2 --sleep 0.1 --lines 2500 --clear_terminal True --marker braille --title "Plotter Test"

read -p ""
plotext bar --path test --xcolumn 1 --title "Bar Plot Test" --xlabel "Animals" --ylabel "Count"

read -p ""
plotext hist --path test --xcolumn 1 --ycolumns 2 --lines 5000 --title "Histogram Test"

read -p ""
plotext image --path test

read -p ""
plotext gif --path test

read -p ""
plotext video --path test --from_youtube True

read -p ""
plotext youtube --url test 
