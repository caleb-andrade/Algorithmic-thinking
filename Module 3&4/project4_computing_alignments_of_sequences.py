# -*- coding: utf-8 -*-
"""
Created on       Wed Aug 05 19:31
Last modified on Thu Aug 06 02:29

@author: Caleb Andrade
"""

def build_scoring_matrix(alph, diag_score, off_diag_score, dash_score):
    """
    This function takes as input a set of characters (alphabet) and three
    scores (diag_score, off_diag_score and dash_score), returns a dictionary
    of dictionaries whose entries are indexed by pairs of characters
    in alphabet plus '-'.
    """
    alphabet = alph.copy()
    alphabet.add('-')
    scoring_matrix = {}
    for row_char in alphabet:
        scoring_matrix[row_char] = {}
        for col_char in alphabet:
            if row_char == col_char and row_char != '-':
                scoring_matrix[row_char][col_char] = diag_score
            elif row_char == '-' or col_char == '-':
                scoring_matrix[row_char][col_char] = dash_score
            else:
                scoring_matrix[row_char][col_char] = off_diag_score
    return scoring_matrix
                

def compute_alignment_matrix(seq_x, seq_y, sco_mat, global_flag):
    """
    Takes as input two sequences seq_x and seq_y whose elements share 
    a common alphabet with the scoring matrix sco_mat. The function 
    computes and returns the alignment matrix for seq_x and seq_y.
    
    If global_flag is True, each entry of the alignment matrix is computed 
    to calculate the global alignment. If global_flag is False, each entry
    is computed to calculate the local alignment.
    """
    ali_mat = [[] for dummy_i in range(len(seq_x) + 1)]
    ali_mat[0].append(0)
    for row in range(1, len(seq_x) + 1):
        temp = ali_mat[row - 1][0] + sco_mat[seq_x[row - 1]]['-']
        if not global_flag and temp < 0:
            ali_mat[row].append(0)
        else:
            ali_mat[row].append(temp)
    for col in range(1, len(seq_y) + 1):
        temp = ali_mat[0][col - 1] + sco_mat['-'][seq_y[col - 1]]
        if not global_flag and temp < 0:
            ali_mat[0].append(0)
        else:
            ali_mat[0].append(temp)
    for row in range(1, len(seq_x) + 1):
        for col in range(1, len(seq_y) + 1):
            opt1 = ali_mat[row - 1][col - 1] + sco_mat[seq_x[row - 1]][seq_y[col - 1]]
            opt2 = ali_mat[row - 1][col] + sco_mat[seq_x[row - 1]]['-']
            opt3 = ali_mat[row][col - 1] + sco_mat['-'][seq_y[col - 1]]
            temp = max([opt1, opt2, opt3])
            if not global_flag and temp < 0:
                ali_mat[row].append(0)                
            else:
                ali_mat[row].append(temp)
    return ali_mat
    
def compute_global_alignment(seq_x, seq_y, sco_mat, ali_mat): 
    """    
    Takes as input two sequences seq_x and seq_y whose elements share 
    a common alphabet with the scoring matrix sco_mat. This function
    computes a global alignment of seq_x and seq_y using the global alignment 
    matrix ali_mat.
    
    The function returns a tuple of the form (score, align_x, align_y) 
    where score is the score of the global alignment align_x and align_y. 
    """
    align_x = ""
    align_y = ""
    score = 0
    row = len(seq_x)
    col = len(seq_y)
    
    while row != 0 and col != 0:
        if ali_mat[row][col] == ali_mat[row-1][col-1] + sco_mat[seq_x[row-1]][seq_y[col-1]]:
            align_x = seq_x[row-1] + align_x
            align_y = seq_y[col-1] + align_y
            row -= 1
            col -= 1
        elif ali_mat[row][col] == ali_mat[row-1][col] + sco_mat[seq_x[row-1]]['-']:
            align_x = seq_x[row-1] + align_x
            align_y = '-' + align_y
            row -= 1
        else:
            align_x = '-' + align_x
            align_y = seq_y[col-1] + align_y
            col -= 1
        score += sco_mat[align_x[0]][align_y[0]]
    
    while row != 0:
        align_x = seq_x[row-1] + align_x
        align_y = '-' + align_y
        row -= 1
        score += sco_mat[align_x[0]][align_y[0]]
    
    while col != 0:
        align_x = '-' + align_x
        align_y = seq_y[col-1] + align_y
        col -= 1
        score += sco_mat[align_x[0]][align_y[0]]
    
    return score, align_x, align_y
    
def compute_local_alignment(seq_x, seq_y, sco_mat, ali_mat): 
    """    
    Takes as input two sequences seq_x and seq_y whose elements share 
    a common alphabet with the scoring matrix sco_mat. 
    This function computes a local alignment of seq_x and seq_y using 
    the local alignment matrix alignment_matrix.
    
    The function returns a tuple of the form (score, align_x, align_y)
    where score is the score of the optimal local alignment align_x and 
    align_y.  
    """
    max_val = [0, 0]
    for idx in range(len(ali_mat)):
        for jdx in range(len(ali_mat[0])):
            if ali_mat[idx][jdx] > ali_mat[max_val[0]][max_val[1]]:
                max_val = [idx, jdx]
    
    align_x = ""
    align_y = ""
    score = 0
    row = max_val[0]
    col = max_val[1]
    
    while ali_mat[row][col] != 0:
        if ali_mat[row][col] == ali_mat[row-1][col-1] + sco_mat[seq_x[row-1]][seq_y[col-1]]:
            align_x = seq_x[row-1] + align_x
            align_y = seq_y[col-1] + align_y
            row -= 1
            col -= 1
        elif ali_mat[row][col] == ali_mat[row-1][col] + sco_mat[seq_x[row-1]]['-']:
            align_x = seq_x[row-1] + align_x
            align_y = '-' + align_y
            row -= 1
        else:
            align_x = '-' + align_x
            align_y = seq_y[col-1] + align_y
            col -= 1
        score += sco_mat[align_x[0]][align_y[0]]
        
    return score, align_x, align_y
    
    
    
        
        
    
            
            
        

       
    
    
    

