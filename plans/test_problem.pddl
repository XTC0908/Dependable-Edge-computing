(define (problem drive)
    (:domain edge_computing_vehicle)
    (:objects v1 - vehicle ob1 - obtacle x - waypoint y - waypoint x1 - waypoint)
    (:init
        (vehicle v1)
        (vehicle-at v1 x)
        (can_traverse v1 x x1)
        (visible x x1)
        ;(not(obtacle_front ob1))
        )
        
        ;(= (total-cost) 0)
    (:goal 
    (and
        (vehicle-at v1 y)
        (not(vehicle-at v1 x))
        ;(imageof ob1)
        ))
       (:metric minimize (total-time))
        )