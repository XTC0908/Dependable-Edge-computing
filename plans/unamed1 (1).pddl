;Objects: 2 vehicles, distance bewteen 2 vehicles 
;Predicates: 
(define (domain edge_computing_vehicle)
    (:requirements :typing :equality :fluents) ;flunets:for total cost
     (:types vehicle coord barrier)
     （:predicates
            (vehilce ?vc - vehicle)
            (vehicle-at ?vc - vehicle ?x ?y - coord)
            (barrier-front ?br - barrier  )
            )
    
    (:action move
        :parameters
            (?vc - vehicle ?x1 ?y1 ?x2 ?y2 - coord)
        :precondition(
            and
            (vehicle-at ?vc ?x1 ?y1)
            (not (barrier-front ?br))
                        )
        :effect (
            and 
            (vehicle-at ?vc ?x2 ?y2)
                 )
    )
            
     