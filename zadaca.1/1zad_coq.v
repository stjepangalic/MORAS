Lemma prvi_a (x y : bool) :
  orb (orb (andb x (negb y)) (andb (negb x) (negb y))) (andb (negb x) y) = orb (negb x) (negb y).
Proof.
  destruct x,y; try reflexivity.
Qed.

Lemma prvi_b (x y z : bool) :
  andb (andb (negb (andb (andb (negb x) y) z)) (negb (andb (andb x y) (negb z))))
  (andb (andb x (negb y)) z) =
   andb (andb x (negb y)) z.
Proof.
  destruct x,y,z; reflexivity.
Qed.