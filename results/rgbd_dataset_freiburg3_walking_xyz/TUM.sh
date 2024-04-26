source activate evo
mkdir Error
mkdir Trajectory
evo_traj tum Original.txt Removed.txt Detected.txt groundtruth.txt -v -p -as --ref=groundtruth.txt --save_plot ./Trajectory/Trajectory_plot.pdf
evo_ape tum groundtruth.txt Original.txt -r full -as --plot --plot_mode xyz --save_plot ./Error/OriginalErrorPlot.pdf --save_results ./Error/OriginalError.zip
evo_ape tum groundtruth.txt Removed.txt -r full -as --plot --plot_mode xyz --save_plot ./Error/RemovedErrorPlot.pdf --save_results ./Error/RemovedError.zip
evo_ape tum groundtruth.txt Detected.txt -r full -as --plot --plot_mode xyz --save_plot ./Error/DetectedErrorPlot.pdf --save_results ./Error/DetectedError.zip

