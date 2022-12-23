# num = int(input("enter you number?\n"))

# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         print("*", end = " ")
#     print()
# # * 
# # * * 
# # * * * 
# # * * * * 
# # * * * * * 
# # ------------------------------------------------

# for row in range(7):
#     for col in range(5):
#         if ((col == 0 or col == 4 ) and row != 0) or\
#              ((row == 0 or row == 3) and (col > 0 and col < 4)):
#             print("*", end = "")
#         else:
#             print(end = " ")
#     print()

# #  *** 
# # *   *
# # *   *
# # *****
# # *   *
# # *   *
# # *   *

# # ---------------------------------------------------


# for row in range(5):
#     for col in range(4):
#         if ((row == 4 or row == 0 or row == 2) or
#          (col==0 or col == 3)):
#             print("*", end = "")
#         else:
#             print(end =" ")
#     print()

# # ****
# # *  *
# # ****
# # *  *
# # ****

# for row in range(5):
#     for col in range(4):
#         if ((col == 0 or col == 3) and (row == 0 or row == 4)):
#             print("*", end = "")
#         else:
#             print(end = " ")
#     print()

# # *  *
    
# # *  *

# # ------------------------------------------------------
# for row in range(5):
#     for col in range(5):
#         if((row == 0 or row == 2 or row == 4 ) and
#          col != 4) \
#            or (col == 0) or (col == 4 and (row !=0 and row != 2 and row != 4))  :
#             print("*", end = "")
#         else:
#             print(end = " ")
#     print()

# # **** 
# # *   *
# # **** 
# # *   *
# # **** 
# # ---------------------------------------------------------

# for row in range(4):
#     for col in range(6):
#         if ((row == 3) or (row == 2 and (col != 0 and col != 5)) or (row == 1 and (col != 0 and col != 1 and col != 5 and col != 4))):
#             print("*", end = "")
#         else:
#             print(end = " ")
#     print()

# #   **  
# #  **** 
# # ******
# # ------------------------------------------------------
# # or mean we have and mean dont have

# # *    *
# # *    *
# # *    *
# # ******
# # *    *
# # *    *
# # *    *
# # ======================================
# # 5 rows
# for name in range(5):
#     # 3 column
#     for j in range(3):
#         print('*', end='')
#     print()

# ***
# ***
# ***
# ***
# ***
# ===================================

row = 5

# Upper-Half
for i in range(row, 0, -1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

# Lower-Half
for i in range(2, row+1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()




# include <stdio.h>

# int main(void){
#     int n = 10;
#     int i = n;
    
#     for(i = n; i >= 1; i--){
	  
# 	  for(int j = n-i; j >= 0; j--){
# 		printf(" ");
# 	}
	
# 	  for(int k = i; k >= 1; k--){
# 		printf("* ");
# 	}
#         printf("\n");
# }

#   if(i == 0){
#   for(i = 2; i <= n; i++){
	  
# 	  for(int j = 0; j <= n-i; j++){
# 		printf(" ");
# 	}
	
# 	  for(int k = 1; k <= i; k++){
# 		printf("* ");
# 	}
#         printf("\n");
# }
  
#   }

# return 0;
# }
