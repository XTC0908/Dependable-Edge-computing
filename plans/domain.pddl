(define (domain edge_computing_vehicle)
    (:requirements :typing :equality :fluents) ;flunets:for total cost
     (:types vehicle waypoint obtacle destination)
     (:predicates
            (vehicle ?vc - vehicle)
            (can_traverse ?vc - vehicle ?x - waypoint ?y - waypoint)  ;can traverse or not
            (vehicle-at ?vc - vehicle ?x - waypoint)
            (obtacle-front ?ob - obtacle)
            (imageof ?ob - obtacle)
            )
            (:functions
                  (total-cost)
                )

    
    (:action move
        :parameters
            (?vc - vehicle ?x - waypoint ?y - waypoint ?ob - obtacle)
        :precondition(
            and
            (vehicle-at ?vc ?x)
            (not(obtacle-front ?ob))
           (can_traverse ?vc ?x ?y)
                        )
        :effect (
            and 
            (vehicle-at ?vc ?y)
            (not(vehicle-at ?vc ?x))
                 )
    )
    (:action take_image    ;when encounter obtacle, take image
   :parameters (?vc - vehicle ?x - waypoint ?y - waypoint ?ob - obtacle )
    :precondition (and (vehicle ?vc)
                    (obtacle-front ?ob))
    :effect (and (imageof ?ob)
    (not(can_traverse ?vc ?x ?y))      ;precossed by the edge ,then can_traverse and not obtacle_front
    )
   )
   )