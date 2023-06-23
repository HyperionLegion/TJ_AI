import sys; args = sys.argv[1:]
import math, random
# t_funct is symbol of transfer functions: 'T1', 'T2', 'T3', or 'T4'
# input is a list of input (summation) values of the current layer
# returns a list of output values of the current layer 
def transfer(t_funct, input):
   if t_funct == "T1":
      return input
   elif t_funct == "T2":
         if input<=0:
            return 0
         return input
   elif t_funct == "T3":
         if input > 100.0:
            return 1.0
         if input < -100.0:
            return 0
         return 1.0/(1.0+math.exp(-1*(input)))
   elif t_funct == "T4":
      return (-1 + 2/(  1+math.exp(-1*input)))
   return input

# example: 4 inputs, 12 weights, and 3 stages(the number of next layer nodes)
# weights are listed like Example Set 1 #4 or on the NN_Lab1_description note
# returns a list of dot_product result. the len of the list == stage
# Challenge? one line solution is possible
def dot_product(input, weights):
   n = 0
   for i in range(0, len(weights)):
      n += weights[i]*input[i]
   return n

# file has weights information. Read file and store weights in a list or a nested list
# input_vals is a list which includes input values from terminal
# t_funct is a string, e.g. 'T1'
# evaluate the whole network (complete the whole forward feeding)
# and return a list of output(s)

def evaluate(input_vals, t_funct, weights):
   counter = 0
   size = []
   output = []
   output.append(input_vals)
   size.append(len(input_vals))
   for i in range(0, len(weights)):
      if(i!=len(weights)-1):
         size.append(1+int(len(weights[i])/size[i]))
      else:
         size.append(int(len(weights[i])/size[i]))
   while(counter < len(weights)):
      values = []
      if(counter != len(weights)-1):
         values.append(1)
      for j in range(0, int(len(weights[counter])/size[counter])):
         # if(counter == len(weights)-1):
         #    values.append(dot_product(output[counter], weights[counter][int(j*size[counter]):int(j*size[counter]+size[counter])]))
         # else:
            values.append(transfer(t_funct, dot_product(output[counter], weights[counter][int(j*size[counter]):int(j*size[counter]+size[counter])])))
      output.append(values)
      counter +=1
   last = output[counter]
   return last[0]
     
def main():
   #args = sys.argv[1:]
   inputs = [[0,0, 0], [0,1,1], [1,0,1], [1,1,0]]
   epochs = 0
   weights = [[ random.random() for i in range (0,9)], [ random.random() for i in range (0,4)]]


   while (epochs < 1000):
      totalerr = 0.0
      
      for i in inputs:
         answer = evaluate([1, i[0], i[1]], 'T3', weights)
         #print(weights)
         #evaluate ff
         error = 0.5 * pow((answer-i[2]), 2)
         totalerr += error
         for j in range(len(weights)):
            for k in range(len(weights[j])):
              # print(weights)
               weights[j][k] = weights[j][k] + 0.01
               #print(weights)
               if(0.5 * pow(evaluate([1, i[0], i[1]], 'T3', weights)-i[2], 2) > error):
                  weights[j][k] = weights[j][k] - 0.02
         #for each weight, test ff with +-0.1 and make a change if error improves
      epochs += 1
      print(epochs, totalerr)
      #print(weights)
   print("Error") #print error
   for i in inputs:
         answer = evaluate([1, i[0], i[1]], 'T3', weights)
         print(i, answer)
if __name__ == '__main__': main()

