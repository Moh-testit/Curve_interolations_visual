##
## EPITECH PROJECT, 2021
## B-MAT-500-COT-5-1-308reedpipes-mohamed.mazu
## File description:
## Makefile
##

NAME	=	308reedpipes

all:	$(NAME)

$(NAME):
		ln -s 308reedpipes.py $(NAME)
		chmod +x $(NAME)

clean:
		rm -rf *~
		rm -rf __pycache__

fclean:	clean
		rm -rf $(NAME)

re:	fclean all
