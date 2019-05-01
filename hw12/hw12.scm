(define (find s predicate)
	(cond
		((equal? s nil) #f)
		((predicate (car s)) (car s))
		(else (find (cdr-stream s) predicate)))
	)


(define (scale-stream s k)
	(define (compute-rest n)
		(scale-stream (cdr-stream s) k))
	(cond 
		((equal? s nil) s)
		(else (cons-stream (* k (car s)) (compute-rest s)))
	)
)

(define (list m)
		(cond 
			((equal? (cdr-stream m) nil) nil)
			(else (cons (cdr-stream m) (list (cdr-stream m))))
		)
)

(define (has-cycle s)

	(define (list m)
		(cond 
			((equal? (cdr-stream m) nil) nil)
			((equal? m (cdr-stream(cdr-stream m))) (cons m 1))
			(else (cons (cdr-stream m) (list (cdr-stream m))))
		)
	)
	(define (compare x y)
		(cond  
			((equal? y nil) #f)
			((equal? x (car y)) #t)
			(else (compare x (cdr y)))
		)
	)

  	(compare s (list s))
)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
