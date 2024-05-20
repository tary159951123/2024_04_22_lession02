{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "min=1\n",
    "max=100\n",
    "count = 0\n",
    "target = random.randint(min,max)\n",
    "print(\"==========猜字遊戲==========\\n\")\n",
    "while True:\n",
    "    count +=1\n",
    "    keyin = pyip.inputInt(f\"猜數字的範圍{min}~{max}\")\n",
    "    if keyin == target:\n",
    "        print(f\"賓果 !猜對了,  答案是{target}\")\n",
    "        print(f\"您總共猜了{count}次\")\n",
    "        break\n",
    "    elif(keyin > target):\n",
    "        print(\"再小一點\")\n",
    "        max = keyin-1\n",
    "    elif(keyin < target):\n",
    "        print(\"再大一點\")\n",
    "        min = keyin + 1\n",
    "    print(f'你已經猜了{count}次')\n",
    "    \n",
    "\n",
    "print(\"遊戲結束\")\n",
    "\n",
    "target"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
