The-Hawk-Dove-game-with-Mesa2

https://the-hawk-dove-game-with-mesa2.herokuapp.com/

Los animales necesitan recursos, como agua y alimento, para vivir. En un ambiente favorable un individuo puede tener más hijos que en un ambiente desfavorable, por ejemplo, supongamos, que en un ambiente favorable un individuo tiene en promedio 5 hijos y en un ambiente desfavorable tiene 2 hijos, podríamos asignarle al recurso un valor de 3 puntos, la diferencia entre la cantidad de hijos que tiene el individuo en un ambiente favorable menos la diferencia de hijos que el individuo tiene en un ambiente desfavorable. Los individuos van sumando puntos, cada recurso aporta una pequeña fracción, y cuando llega a una determinada edad el individuo se reproduce asexualmente, crea copias de sí mismo de acuerdo a la cantidad de puntos obtenidos, y luego muere.

Las plantas no se dejan comer, producen sabores desagradables, los animales tampoco se dejan comer, las gacelas evolucionan para correr más rápido, haciéndoles hacen cada vez la vida más difícil a los leones. En este modelo no vamos a considerar  la carrera armamentística asimetría, esto es, como evolucionan las presas y los depredadores. Nosotros vamos a suponer que en cada posición del tablero,  el ambiente donde se desarrolla el juego, hay recursos que los animales necesitan para vivir.

Un recurso se puede compartir. Si bien hay situaciones en las cuales a los individuos no les conviene compartir un recurso, por ejemplo si un ambiente favorable tiene para el animal 10 puntos, y un ambiente menos favorable tiene 8 puntos, a nadie le convendría compartir y tener  5 putos. En este modelo supondremos que los recursos son divisibles y que a los animales les conviene compartir. 

Un conflicto se produce cuando dos individuos quieren el mismo recurso. Los conflictos se pueden resolver en forma pacífica, compartiendo el recurso, o escalando, peleando hasta que uno de los dos queda gravemente lesionado.   Las lesiones producidas en un combate entre dos animales son costosas, también es un costo, aunque menor, el tiempo perdido amenazando al contrincante, gruñendo o mostrándole los dientes.

La peleas entre animales se parecen más a una guerra de desgaste asimétrica  que a un juego de halcones y palomas. En una guerra de desgaste ambos contrincantes, el ganador y el perdedor,  pagan el mismo costo, la menor cantidad de golpes que estaba dispuesto a recibir el perdedor.  Por ejemplo, supongamos que un contrincante está dispuesto a pelear hasta que tenga el ojo en compota y el rival hasta las costillas rota. Empieza la pela, un contrincante tira un puño y le rompe el tabique nasal, como los contrincantes son físicamente iguales, el otro tira en puño y le rompe el tabique nasal al otro. Así hasta que llegan a los ojo en compota, momento en que uno de los contrincantes se retira y el otro gana. En este caso gana el animal que estaba dispuesto a pelear hasta tener una costilla rota y ambos animales pagan el costo de romperse el tabique nasal.  Este no es el modelo implementado, el modelo que implemente,  halcones y palomas, solo el perdedor paga un costo fijo y el ganador obtiene el recurso sin resultar lesionado.

Sabemos que el altruismo puede evolucionar si un individuo puede reconocer a individuos altruistas y ayudar solo a los que reconoció como altruista, si un individuo altruista se tira a un rio para salvar 10 individuos el altruistas podría morir, pero el gen para altruismo podría evolucionar si salvo a 10 individuos. De igual manera la cooperación puede evolucionar en un dilema del prisionero repetido, si hay reconocimiento individual de los miembros de la población cooperar si el contrincante colaboro con migo en el paso y desertar si deserto. Estos los casos, altruismo y cooperación, los modelos suponen reconocimiento individual y memoria. En el modelo que  implemente no hay reconocimiento, ni memoria, el individuo son anónimos, no saben, antes de comenzar la pelea si el oponente es violento o pacifico, y tampoco queda recuerdo en la memoria de combate con el individuo.

La cantidad de hijos que un padre tiene depende de los recursos y las lesiones sufridas. Los individuos viven una determinada edad se reproducen y luego mueren, por ejemplo pueden vivir 6 pasos de simulación  dejar 2 hijos. Los hijos son iguales que sus padres, son clones de sus padres ya que en el modelo la reproducción es asexual, heredan la misma forma de resolución de conflictos.  Si los padres resolvían los conflictos compartiendo, los hijos van a compartir, si los padres resolvían las disputas peleando los hijos van a resolver las disputas peleando. El final del juego habrá más individuos que compartan y más individuos violentos.
La explosión demográfica es un problema en la simulación. En la naturaleza las poblaciones no crecen hasta quedarse sin recurso. Si en la simulación hacemos que los individuos más aptos tengan más de 2 hijos el crecimiento es exponencial y en pocas generaciones se produce una sobrepoblación. En cambio si hago que los individuos más aptos tengan un solo hijo, y los menos aptos no tengan ningún hijo,  en cada generación se va reduciendo. Los biólogos propusieron varias explicaciones. Una explicación es selección de grupo, los individuos se reúnen, hacen un censo y se decide, inconscientemente, cuantos descendientes se tendrá en la próxima generación. Otra solución, más realista, es pensar en un problema de optimización. Tener un hijo tiene un coste y solo se obtiene una ganancia si el hijo  llega sano y salvo a la edad adulta y le dé nietos. En la población hay individuos que están genéticamente programados para tener 20 hijos, hay individuos que están programados para temes 10 y los hay que tiene 5 hijos. Si un individuos pone 20 huevos y no puede alimentar a todos, todos mueren y deja menos descendía de alguien que solo pone 5 huevos y los 5 hijos llegan a la edad adulta. Esto da como resultado una regulación dinámica de la cantidad de hijos óptimos.  Para esta simulaciones se implementó una política centralizada, se cuanta la cantidad total de individuos de la población y en base a esto se decide cuantos hijos tendrán en la próxima generación los más aptos y cuantos hijos tendrán los menos aptos.

Se van a implementar 3 modelos. En uno todos los individuos son iguales, tienen el mismo tamaño, la misma fuerza física, las estrategias de los individuos son compartir y pelear.  En el otro modelo hay individuos distintos pero que no influye en la fuerza física, ni en la capacidad de lucha, por ejemplo el color de pelo, unos con barba verde y otro que se afeitan la barba, uno que rompen los huevos por las punta y otro por el medio. Se agregan estrategias condicionales, si mi oponente tiene el pelo más oscuro que el mío peleo, en caso contrario comparto. En el último modelo hay individuos grandes y chicos, los individuos grandes tienen más probabilidad de ganarle a alguien pequeño. En este modelo además de compartir y cooperar están las estrategias pelear si mi contrincante es de menor tamaño.

Compartir o pelear en población donde todos los individuos son iguales
En el primer modelo que implementamos suponemos que todos los individuos son exactamente iguales, no se diferencian en nada, hasta que surge un conflicto. En lo único que se diferencian es en la forma que usan para resolver un conflicto.  Como los individuos son físicamente exactamente iguales, la probabilidad de que uno gane es del 50% y la probabilidad de que  gane el otro  es del 50%.  No sabe qué estrategia va a usar el oponente, no es una opción  una estrategia condicional del tipo colaborar si el otro es de los colaboradores, además no hay memoria, ni recuerdo de las peleas pasadas, las estrategias de resolución de conflicto son hereditarias. 

La Todos los individuos ante un conflicto comparten o pelean. Loa individuos que comparten tuvieron un padre que compartía y los individuos que pelean tuvieron un padre que peleaba. Una de las estrategias es compartir. Se comparte si el otro también quiere compartir,  si el otro no quiere compartir, quiere pelear por el recurso, el que quiere compartir le cede el recurso al violento. La otra estrategia pelear, pelea hasta conseguir el recurso y hasta quedar gravemente lesionado.  Si elijo pelear y el otro elije pelear se da una pelea y dado que somos iguales físicamente se tiene el 50% de probabilidades de ganar y 50% de probabilidades de terminar gravemente lesionado.  

Veremos si al final de los juegos hay más individuos que resuelven sus conflictos a los golpes o deciden compartir.  Qué pasa si en una población donde todos comparten se agrega un violento? Puede invadir la población? Que pasa con una población donde todos son violentos y se agrega uno que comparte? 

Todo depende del valor del recurso y del coste de la lesión. Si el valor del recurso es superior al costo de lesión una población violenta no puede ser invadido por alguien que comparta y si en la población inicial todos están compartiendo y se agrega un violento, el violento invade la población y toda la población se vuelve violenta al final de juego.

Por ejemplo, si todos los individuos eligieron pelear y el costo de lesión es superior al valor del recurso a mí me conviene elegir compartir, porque si bien mi ganancia neta va a ser 0, voy a ceder con todos, no voy a ganar nunca, si elijaría pelear la mitad de las veces ganaría y la otra mitad de las veces perdería, la mitad de las veces obtendría el recurso y la otra mitad de las veces quedaría lesionado, y dado que la lesión es mayor que el beneficio del recuso, obtendría en promedio un resultado menor que cero.

En resumen, si valor del recurso es mayor que el costo de perder una pelea y tengo una población pacifica con solo agregar un individuo violento, que en vez de compartir prefiera pelear, al final del juego todos los individuos van a ser violentos. Si el valor del recurso es menor que el costo de lesiones al final del juego voy a tener en la población un porcentaje de sujetos que prefieren compartir y un porcentaje de violentos, mientras mayor sea el costo por perder una pelea mayor va a ser el porcentaje de la población que va a preferir ser pacífica y compartir recursos en conflicto. Una conclusión interesante es que por más grande que sea el coste de lesión siempre habrá un pequeño porcentaje que le rendirá ser violento. 


Estrategias condicionales usando diferencias arbitrarias entre los individuos

En la vida real no somos clones, no somos todos iguales, hay diferencias como el tamaño y la fuerza y esto  influyen en el resultado de un combate, también  hay diferencias como el color de piel, el color de cabello, tener barba verde que no tiene ninguna influencia en el resultado de una pelea.  Primero vamos a considerar individuos que son diferentes en atributos que no influyen en el resultado de un combate, como tener barba verde, tener cabello oscuro o claro. Luego vamos a considerar las diferencias que si influyen en el resultado de una pelea, como ser más grande y más fuerte.

Supongamos que algunos individuos  tienen barba verde y otros  no. Ahora yo puedo considerar 3 estrategias, una estrategia es siempre compartir, la otra estrategia es siempre pelear y una tercera estrategia es pelear solo si mi contrincante tiene barba verde, en los demás casos compartir. Que sucede en este caso, que estrategia me conviene a mi adoptar? Si toda la población pelea solo si su contrincante tiene barba verde y en los demás casos comparte, si yo tengo barba verde y elijo compartir voy a tener cero, si elijo pelear  voy a perder la mitad de las peleas y lesionados la otra mitad de las peleas y si elijo pelear solo si el contrincante tiene barba verde y compartir en caso contrario voy a perder un cuarto de las peles y estar lesionado un cuarto de las peles, que es mejor que estar lesionado la mitad de las peleas y ganar la mitad de las peleas, si el costo de una lesión es mayor que el beneficio del recurso. Ahora suponiendo que no tenga barba verde voy a llegar a un resultado similar. Por lo tanto si todos están peleando con los que tienen barba verde, a mí me conviene elegir la misma estrategia incluso si yo también tengo barba verde.

Supongamos que hay individuos que tienen cabello claro y caballo oscuro, además suponemos que cada individuo sabe su color de cabello y puede ver el color de cabello de su oponente, pero no puede saber si su oponente va a compartir el recurso o va a pelear.  Con estas nuevas capacidades que ahora consideramos que tienen todos los individuos de la población podemos agregar otra estrategia. Además de la estrategia  siempre compartir, siempre pelear  agregamos una tercera estrategia es pelear solo si mi contrincante tiene el cabello más oscuro que mi color de cabello y compartir en caso contrario. Que sucederá en este caso? qué estrategia me conviene a mi adoptar para ganar más puntos?

Si mi color de cabello es claro, las estrategias pelear si mi contrincante tiene cabello oscuro y compartir caso contrario y la estrategia siempre compartir obtengo los mismos puntos, comparto el recurso con la mitad de la población. La estrategia siempre pelear gano la mitad de las veces y pierdo la otra mitad. Si son muy costosas las lesiones me conviene compartir el recurso con la mitad de la población que ganar el recurso la mitad de las veces y resultar lesionadas la otra mitad de las veces. Por lo tanto si todos están peleando con los que tienen cabello oscuro, a mí me conviene elegir la misma estrategia que eligieron todos.

Por ejemplo, si todos los individuos eligieron pelear a mí me conviene elegir compartir, porque si bien mi ganancia neta va a ser 0, voy a ceder el recurso a todos, si elijaría pelear, como somos iguales,  la mitad de las peleas ganaría y la otra mitad las perdería, la mitad de las veces obtendría el recurso y la otra mitad de las veces quedaría lesionado, y dado que coste de lesión es mayor que el valor  de recuso, obtendría en promedio un resultado menor que cero. Por otro lado si todos los individuos están compartiendo a mí me conviene pelear, ya que en una contienda con alguien que comparte solo se rendiría y cedería el recurso sin luchar. Si hubiera elegido compartir obtendría la mitad del recurso que es menor a todo el recurso.

Diferencias entre individuos en aspectos que influyen en el resultado de una pelea
Ahora consideremos el caso de una población donde los individuos son distintos pero en cosas que influyen en el resultado de una pelea, por ejemplo en la población hay individuos grandes y fuertes e individuos pequeños y débiles y la influencia que tiene lo que está haciendo la mayoría de la población en mi elección de qué estrategia seguir.

Supongamos que tenemos una población de 20 individuos asimétricos. Una asimetría puede ser el tamaño, hay individuos grandes e individuos chicos, otro ejemplo de asimetría puede ser el sexo, hay individuos que son machos y otros que son hembras. Para simplificar asumamos que la asimetría puede tener solo dos valores, por ejemplo grande o chico, no hay individuos mas o menos grandes, ni individuos de 62 kgm, solo podemos clasificar a los individuos en grandes o chicos. En una pelea entre dos individuos grandes existe la misma probabilidad de que gane uno o de que gane el otro, igualmente una pelea entre individuos chicos tenemos el 50% de probabilidad de que gane uno o de que gane el otro. Pero cuando se enfrenta un individuo grande contra un individuo chico la probabilidad de que gane el mas grande es un parámetro del modelo. Si el mas grande siempre gana ponemos un porcentaje de 100, si en peleas entre grandes y chicos el 80% de las veces gana el mas grande ajustamos el parámetro del modelo a 80.

Supongamos que en la población hay tres estrategias, siempre compartir, siempre pelear y pelear solo si soy más débil y pequeño y compartir si soy más fuerte y grande. Supongamos que toda la población está siguiendo la estrategia condicional paradójica, pelear si soy el más débil y pequeño que mi rival y compartir si soy más grande y fuerte. Si en esta población alguien que es grande y fuerte elije siempre pelear, se va a pelear con todo el mundo y va a obtener un resultado peor que alguien que hubiera elegido la estrategia condicional paradójica.

Si los machos son más fuertes y grandes que las hembras, el 90% de las peleas entre hembras y machos las gana un macho, una estrategia condicional paradójica del tipo si sos hembra y tu contrincante es un macho atacar,  y si sos macho y tu contendiente es una hembra huir podría sser una estrategia evolutivamente estable. Cualquiera que hiciera algo distinto estaría en desventaja, las estrategias siempre huir, siempre pelear están en desventaja contra la estrategia condicional paradójica que estaría haciendo la mayoría de la población. Una pregunta es como se llegaría a que la mayoría de la población adopte la estrategia paradijica, las etapas intermedias no serian evolutivamente estables.

Juegos con estrategias evolutivas inestables
Un último juego. Dos tipos de jugadores, machos y hembras. Dos tipos de estrategia para cada uno de los tipos de jugadores. Los machos pueden ser fieles o atorrantes y las hembras pueden ser fáciles y santas. Supongamos que la ventaja evolutiva por tener una  cría le da 15 puntos a cada uno de los padres, supongamos que el coste para tener una criar una cría con éxito es de 20 puntos, este coste se puede repartir entre los padres o lo pude pagar solo la hembra dependiendo del tipo de estrategia, supongamos que en un cortejo se pierden 3 puntos.

En un encuentro de macho atorrante con una hembra fácil, le da al macho 15 puntos y a la hembra -5 puntos.

Un encuentro entre un macho fiel y una hembra santa, el macho gana 2 puntos, esto es 15 de la cría -10 de la crianza compartida, -3 del cortejo. La hembra también obtiene el mismo puntaje.

Un encuentro entre un macho atorrante y una hembra santa cada uno obtiene 0 puntos, no tienen ninguna cría, no hay cortejo, ni hay costo de crianza.

Un encuentro entre un macho fiel y una hembra fácil, el macho consigue 5 puntos y la hembra también consigue 5 puntos.

Si se analiza el juego parecería que hay un equilibrio estable en. Pero se puede ver que en realidad es un equilibrio inestable, el juego oscila, una vez que se alcanza el equilibrio, si se produce una pequeña modificación en los porcentajes, lejos de autorregularse y volver al equilibrio, el desequilibrio se potencia hasta alcanzar un equilibrio distinto.

 


 




 




 

///////////////

 

Los individuos necesitan determinados recursos para vivir, cuando un individuo llega a una determinada edad crea copias de sí mismo y muere. La cantidad de copias que genera cada individuo depende de los puntos conseguidos y de la cantidad total de individuos en la población

 

Los individuos se disputan los recursos escasos que hay en un ambiente. Hay varias formas en que los individuos pueden resolver los conflictos. Una de las estrategias es intentar compartir el recurso, y si el otro no está dispuesto a compartir el recurso y quiere escalar la pelea, nos retiramos y le dejamos el recurso al oponente, otra estrategia es escalar la pelea si el oponente es más pequeño,  más pequeño significa que tenemos mayor probabilidad de ganar una pelea cuando escala y la última estrategia es siempre escalar, nunca compartir.

 

Cuando un individuo llega a la edad de reproducción hace copias de sí mismo. La cantidad de copias que el individuo va a hacer depende no solo de su pontaje sino que depende también de la cantidad de individuos que hay en la población. Los puntos que los individuos obtuvieron en los combates  se convierten a una escala del 0 al 100. Los que tienen 100 son los individuos que más puntos obtuvieron y los que tienen 0 son los individuos que menos puntos obtuvieron.

 

Si la población es de menos de 50 individuos y el sujeto obtiene menos de 50 en la generación siguiente habrá una sola copia de sí mismo, si tiene más de 50 puntos hace 2 copias de sí mismo.

 

Si la población esta entra 50 y 100 y el sujeto obtiene menos de 33 no hace copias de sí mismo, si tiene entre 33 y 66 hace 1 copia de sí mismo, si tiene más de 66 hace dos copias de sí mismo.

 

Los descendientes heredan la misma estrategia que los padres. Si los padres son de escalar sus descendientes tienen las mismas estrategias de resolución de conflicto.

 

Luego de la reproducción el individuo muere.

 

La cantidad de descendientes no solamente depende la aptitud del individuos (la cantidad de puntos que el individuo consiguió) sino también de la cantidad de individuos en la población (si hay muchos individuos los individuos tendrán menos hijos). La forma en que los animales regulan la población son vas. Una de las formas es que hay individuos que tienen 5 hijos, hay individuos que tienen 2 hijos, esto es una distribución de probabilidades de cantidad de hijos. Si en la población hay pocos individuos, esto es, hay muchos recursos, los que tengan 5 hijos van a tener ventajas, si hay muchos individuos, los que están genéticamente programados para tener 5 hijos, van a morir de hambre los 5 hijos y van a estar en desventaja con los que tienen 1 hijo.

 

Para este proyecto se decido una política de regulación de población centralizada, alguien sabe la cantidad total de individuos de la población y regula la cantidad de hijos de acuerdo a ese dato, esto es poco realista pero fácil de implementar.
Podemos suponer que existen individuos igualmente aptos, esto es que obtuvieron la misma cantidad de puntos,  que tienen distinta cantidad de descendientes, por ejemplo uno pone 2 huevos y el otro pone 5 huevos. Podríamos pensar que poner 5 huevos es mejor que poner 2, pero esto no es siempre verdadero. Puede ser que se hayan agotado los recursos del ambiente y el que pone 5 huevos no los puede alimentar y mueren los 5, mientras que 2 huevos es, en este caso, el tamaño óptimo. Serian dos variables independientes, una la aptitud, y la otra la cantidad de descendientes óptimos. Si sos muy apto pero estas programado genéticamente para poner una cantidad de huevos muy grande, van a morir todos y no vas a dejar descendientes.

