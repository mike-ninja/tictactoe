# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    controller.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbarutel <mbarutel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/08 19:48:45 by mbarutel          #+#    #+#              #
#    Updated: 2023/03/08 19:49:20 by mbarutel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import model

class Controller():
    def __init__(self):
        self.init_model()
        
    def init_model(self):
        self.model = model.Model()