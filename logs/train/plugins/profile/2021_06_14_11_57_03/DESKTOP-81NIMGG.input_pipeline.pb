	0*?p??@0*?p??@!0*?p??@	q????C@q????C@!q????C@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$0*?p??@??|?5^??A?Ǻ??@Y?2ı.J\@*	ffff???@2?
JIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[0]::MapNё\??X@!?6?|UV@)?z?G?X@1?Oe?eV@:Preprocessing2k
4Iterator::Model::MaxIntraOpParallelism::Map::BatchV2|a2U[@!?A?$?W@)?Y??ڊ@1}?K?]?@:Preprocessing2b
+Iterator::Model::MaxIntraOpParallelism::Map??ǘ?B\@!Q??cx?X@)ffffff@1?v? FE@:Preprocessing2y
BIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip?St$?Y@!?|A??3V@)g??j+???1???CC??:Preprocessing2?
RIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[1]::TensorSlice?Zd;??!?-?p???)?Zd;??1?-?p???:Preprocessing2t
=Iterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle?&?#Y@!??B&?:V@)T㥛? ??1??#腼?:Preprocessing2?
WIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[0]::Map::TensorSliceгY??ں?!?Y?s ???)гY??ں?1?Y?s ???:Preprocessing2]
&Iterator::Model::MaxIntraOpParallelism?D??D\@!K?+9l?X@)D?l?????1???rS=??:Preprocessing2F
Iterator::Model?j+??E\@!      Y@)??ZӼ???1??V??x??:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 3.4% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9r????C@I???X?%X@Zno#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	??|?5^????|?5^??!??|?5^??      ??!       "      ??!       *      ??!       2	?Ǻ??@?Ǻ??@!?Ǻ??@:      ??!       B      ??!       J	?2ı.J\@?2ı.J\@!?2ı.J\@R      ??!       Z	?2ı.J\@?2ı.J\@!?2ı.J\@b      ??!       JCPU_ONLYYr????C@b q???X?%X@