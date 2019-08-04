(define (cube x)
  (* x x x)
)

(define (over-or-under x y)
  ; (if (< x y) 
  ; 	  -1
  ; 	  (if (= x y) 
  ; 	  	   0
  ; 	       (if (> x y)
  ; 	  	  1))
  ; )
	(cond ((< x y) -1)
		  ((= x y) 0)
		  ((> x y) 1))
)

(define (make-adder num)
  		(define (procedure x)
  			(+ x num))
  		procedure
)

(define structure
  (cons (cons 1 nil)
  		(cons 2 
  			    (cons (cons 3  4)
  			    	  (cons 5 nil))))
)

(define (remove item lst)
	(cond ((null? lst) lst)
		  ((= (car lst) item) (remove item (cdr lst)))
  		  (else (cons (car lst) (remove item (cdr lst)))))
)

