# Sample input: x_gate.txt

import sys, os, math, random

# t_funct is symbol of transfer functions: 'T1', 'T2', 'T3', or 'T4'
# input is a list of input (summation) values of the current layer
# returns a list of output values of the current layer
def transfer(t_funct, input):
   if t_funct == 'T3': return [1 / (1 + math.e**-x) for x in input]
   elif t_funct == 'T4': return [-1+2/(1+math.e**-x) for x in input]
   elif t_funct == 'T2': return [x if x > 0 else 0 for x in input]
   else: return [x for x in input]

# returns a list of dot_product result. the len of the list == stage
# dot_product([x1, x2, x3], [w11, w21, w31, w12, w22, w32], 2) => [x1*w11 + x2*w21 + x3*w31, x1*w12, x2*w22, x3*w32] 
def dot_product(input, weights, stage):
   return [sum([input[x]*weights[x+s*len(input)] for x in range(len(input))]) for s in range(stage)]

# Complete the whole forward feeding for one input(training) set
# return updated x_vals and error of the one forward feeding
def ff(ts, xv, weights, t_funct):

   ''' ff coding goes here '''
   counter = 0
   while(counter < len(weights)-1):
      counter +=1
      xv[counter] = transfer(t_funct, dot_product(xv[counter-1], weights[counter-1], int(len(weights[counter-1])/len(xv[counter-1]))))
   counter+=1
   xv[counter] = dot_product(xv[counter-1], weights[counter-1], int(len(weights[counter-1])/len(xv[counter-1])))
   err = (ts[-1] - xv[-1][0])**2 / 2
   return xv, err

# Complete the back propagation with one training set and corresponding x_vals and weights
# update E_vals (ev) and negative_grad, and then return those two lists
def bp(ts, xv, weights, ev, negative_grad):   

   ''' bp coding goes here '''
   counter = len(ev)-1
   err = (ts[-1] - xv[-1][0])
   ev[counter][0] = err
   counter = counter - 1
   while(counter>=1):
      for i in range(0,len(xv[counter])):
         err = 0
         for j in range(0, len(ev[counter+1])):
            err = err + ev[counter+1][j]
         ev[counter][i] = err*xv[counter][i]*(1-xv[counter][i])*weights[counter][i]
      counter = counter - 1
   counter = len(weights)-1
   for i in range(0, len(ev[counter])):
         for j in range(0, len(weights[len(weights)-1])):
            negative_grad[counter][i] = (ts[-1] - xv[-1][0]) * xv[counter][j]
   counter = counter - 1
   while(counter>=0):
      for i in range(0, len(ev[counter])):
         for j in range(0, len(ev[counter+1])):
            negative_grad[counter][i*len(ev[counter+1])+j] = ev[counter+1][j] * xv[counter][i]
            # print('new')
#             print(i)
#             print(j)
#             print(len(ev[counter+1]))
#             print(ev[counter+1][j] * xv[counter][i])
      counter = counter - 1
#    print(xv)
#    print(ev)
#    print(negative_grad)
   return ev, negative_grad
   

# update all weights and return the new weights
# Challenge: one line solution is possible
def update_weights(weights, negative_grad, alpha):

   ''' update weights (modify NN) code goes here '''
#    print(weights)
#    print(negative_grad)
   for i in range(0,len(weights)):
      for j in range(0,len(weights[i])):
         weights[i][j] = weights[i][j]+alpha*negative_grad[i][j]
   return weights

def main():
   file = sys.argv[1] # only one input (a txt file with training set data)
   if not os.path.isfile(file): exit("Error: training set is not given")
   t_funct = 'T3' # we default the transfer(activation) function as 1 / (1 + math.e**(-x))
   training_set = [[float(x) for x in line.split() if x != '=>'] for line in open(file, 'r').read().splitlines() if line.strip() != '']
   #print (training_set) #[[1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [-1.0, -1.0, 1.0], [0.0, 0.0, 0.0]]
   layer_counts = [len(training_set[0]), 2, 1, 1]
   print ('layer counts', layer_counts) # This is the first output. [3, 2, 1, 1] with teh given x_gate.txt

   ''' build NN: x nodes and weights '''
   x_vals = [[temp[0:len(temp)-1]] for temp in training_set] # x_vals starts with first input values
   #print (x_vals) # [[[1.0, -1.0]], [[-1.0, 1.0]], [[1.0, 1.0]], [[-1.0, -1.0]], [[0.0, 0.0]]]
   # make the x value structure of the NN by putting bias and initial value 0s.
   for i in range(len(training_set)):
      for j in range(len(layer_counts)):
         if j == 0: x_vals[i][j].append(1.0)
         else: x_vals[i].append([0 for temp in range(layer_counts[j])])
   #print (x_vals) # [[[1.0, -1.0, 1.0], [0, 0], [0], [0]], [[-1.0, 1.0, 1.0], [0, 0], [0], [0]], ...

   # by using the layer counts, set initial weights [3, 2, 1, 1] => 3*2 + 2*1 + 1*1: Total 6, 2, and 1 weights are needed
   weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-1)]
   #weights = [[1.35, -1.34, -1.66, -0.55, -0.9, -0.58, -1.0, 1.78], [-1.08, -0.7], [-0.6]]   #Example 2
   # print (weights)    #[[2.0274715389784507e-05, -3.9375970265443985, 2.4827119599531016, 0.00014994269071843774, -3.6634876683142332, -1.9655046461270405]
                        #[-3.7349985848630634, 3.5846029322774617]
                        #[2.98900741942973]]

   # build the structure of BP NN: E nodes and negative_gradients 
   E_vals = [[*i] for i in x_vals]  #copy elements from x_vals, E_vals has the same structures with x_vals
   negative_grad = [[*i] for i in weights]  #copy elements from weights, negative gradients has the same structures with weights
   errors = [10]*len(training_set)  # Whenever FF is done once, error will be updated. Start with 10 (a big num)
   count = 1  # count how many times you trained the network, this can be used for index calc or for decision making of 'restart'
   alpha = 0.3
   #print ('weights:')
   #for w in weights: print (w)
   # calculate the initail error sum. After each forward feeding (# of training sets), calculate the error and store at error list
   for k in range(len(training_set)):
      x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
      #sum??
      #bp
      E_vals[k], negative_grad = bp(training_set[k], x_vals[k], weights, E_vals[k], negative_grad)
      #modify weights
      update_weights(weights, negative_grad, alpha)
   err = sum(errors)
   
   ''' 
   while err is too big, reset all weights as random values and re-calculate the error sum.
   
   '''
   while(err>1):
        weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-1)]
        for k in range(len(training_set)):
          x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
          err = sum(errors)
   while(err>0.005 and count < 45000):
        if(count%1500==0):
               #print(err)
               weights = [[round(random.uniform(-2.0, 2.0), 2) for j in range(layer_counts[i]*layer_counts[i+1])]  for i in range(len(layer_counts)-1)]
        for k in range(len(training_set)):
          x_vals[k], errors[k] = ff(training_set[k], x_vals[k], weights, t_funct)
          #sum??
          #bp
          E_vals[k], negative_grad = bp(training_set[k], x_vals[k], weights, E_vals[k], negative_grad)
          #modify weights
          update_weights(weights, negative_grad, alpha)
        err = sum(errors)
        count+=1
        
   #print(count)
   #print(err)
    #print(x_vals)
   ''' 
   while err does not reach to the goal and count is not too big,
      update x_vals and errors by calling ff()
      whenever all training sets are forward fed, 
         check error sum and change alpha or reset weights if it's needed
      update E_vals and negative_grad by calling bp()
      update weights
      count++
   '''
   # print final weights of the working NN
   print ('weights:')
   for w in weights: print (w)
if __name__ == '__main__': main()