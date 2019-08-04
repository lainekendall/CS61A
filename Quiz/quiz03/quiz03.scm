; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

(define (map f s)
  (if (null? s) s
    (cons (f (car s)) (map f (cdr s)))))

(define (filter f s)
  (if (null? s) s
    (let ((rest (filter f (cdr s))))
      (if (f (car s)) (cons (car s) rest) rest))))

(define (contains? s v)
    (cond ((null? s) #f)
          ((= v (car s)) #t)
          ((> (car s) v) #f)
          (else (contains? (cdr s) v))
          ))


(define (remove item lst)
	(cond ((null? lst) lst)
		  ((= (car lst) item) (remove item (cdr lst)))
  		  (else (cons (car lst) (remove item (cdr lst)))))
)

(define (no-repeats s)
  (define (helper s new)
  	(cond ((null? s) s)
  		  (else (cons (car s) (helper (remove (car s) s) (cons (car s) new))))
  ))
  (helper s nil)
  )

(define (how-many-dots s)
  (cond ((null? s) 0)
  		((number? (car s)) (cond ((number? (cdr s)) 1)
  								 (else (how-many-dots (cdr s)))))
  		(else (cond ((number? (cdr s)) (+ 1 (how-many-dots (car s))))
  					(else (+ (how-many-dots (car s)) (how-many-dots (cdr s))))))
  		)
  )
