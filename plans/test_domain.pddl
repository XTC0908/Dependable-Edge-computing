(define (domain edge_computing_vehicle)
    (:requirements :typing :equality :fluents) ;flunets:for total cost
     (:types vehicle waypoint obtacle destination)
     (:predicates
            (vehicle ?vc - vehicle)
            (can_traverse ?vc - vehicle ?x - waypoint ?y - waypoint)  ;can traverse or not
            (vehicle-at ?vc - vehicle ?x - waypoint)
            (obtacle-front ?ob - obtacle)
            ;(imageof ?ob - obtacle)
            (visible ?x - waypoint ?y - waypoint ) 
            )
            (:functions
                  (total-cost)
                )

    
    (:action move
        :parameters
            (?vc - vehicle ?x - waypoint ?y - waypoint ?ob - obtacle ?x1 - waypoint)
        :precondition(
            and
            (vehicle-at ?vc ?x)
            (not(vehicle-at ?vc ?y))
            (visible ?x ?x1)
            (not(obtacle-front ?ob))
           (can_traverse ?vc ?x ?x1)
                        )
        :effect (
            and 
            (vehicle-at ?vc ?y)
            (not(vehicle-at ?vc ?x))
                 )
    )
   ;(:action take_image    ;when encounter obtacle, take image
   
    ;:parameters (?vc - vehicle ?x - waypoint ?y - waypoint ?ob - obtacle )
    ;:precondition (and (vehicle ?vc)
     ;               (vehicle-at ?vc ?x)
      ;             (obtacle-front ?ob)
                   ;(not(imageof ?ob))
       ;            )
    ;:effect (and (imageof ?ob)
   ;)   ;processed by the edge ,then can_traverse and not obtacle_front
    
  ; )
   ;(:action replan
   ;:parameters (?vc - vehicle ?x - waypoint ?y - waypoint ?ob - obtacle)
   ;:precondition (and (vehicle-at ?vc ?x)
    ;                (vehicle ?vc)
     ;               (imageof ?ob))
    ;:effect (and
    ;(vehicle-at ?vc ?y)
    ;(not(imageof ?ob))
    ;(not(vehicle-at ?vc ?x)))
   ;)
   )
   