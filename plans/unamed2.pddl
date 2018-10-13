(define (problem drive))
    (:domain edge_computing_vehicle)
    (:objects v1 - vehicle)
    (:init
        (vehicle-at v1 x1 y1))
    (:goal 
    (and
        (vehicle-at v1 x2 y2)
        (not (barrier-front br))
        )
        (:metric minimize (totalCost))
        )