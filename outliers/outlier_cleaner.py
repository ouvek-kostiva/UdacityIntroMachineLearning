{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'predictions' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-e984b912f72e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     21\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mcleaned_data\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     22\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 23\u001b[1;33m \u001b[1;32mprint\u001b[0m \u001b[0moutlierCleaner\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpredictions\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mages\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnet_worths\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'predictions' is not defined"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/python\n",
    "\n",
    "\n",
    "def outlierCleaner(predictions, ages, net_worths):\n",
    "    \"\"\"\n",
    "        Clean away the 10% of points that have the largest\n",
    "        residual errors (difference between the prediction\n",
    "        and the actual net worth).\n",
    "\n",
    "        Return a list of tuples named cleaned_data where \n",
    "        each tuple is of the form (age, net_worth, error).\n",
    "    \"\"\"\n",
    "    \n",
    "    cleaned_data = []\n",
    "\n",
    "    ### your code goes here\n",
    "    errors = net_worths - predictions\n",
    "    threshold = numpy.percentile(numpy.absolute(errors), 90)\n",
    "    cleaned_data = [(age, net_worth, error) for age, net_worth, error in zip(ages, net_worths, errors) if abs(error) <= threshold]\n",
    "    \n",
    "    return cleaned_data\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
