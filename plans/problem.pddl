(define (problem drive)
    (:domain edge_computing_vehicle)
    (:objects v1 - vehicle ob1 - obtacle x - waypoint y - waypoint)
    (:init
        (vehicle v1)
        (vehicle-at v1 x))
        ;(= (total-cost) 0)
    (:goal 
    (and
        (vehicle-at v1 y)
        (not(vehicle-at v1 x))
        ))
       (:metric minimize (total-time))
        )