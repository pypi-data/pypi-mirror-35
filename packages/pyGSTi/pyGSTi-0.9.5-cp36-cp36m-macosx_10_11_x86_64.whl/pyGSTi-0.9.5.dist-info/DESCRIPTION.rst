Gate set tomography (GST) is a quantum tomography protocol that provides full characterization of a quantum logic device (e.g. a qubit).  GST estimates a set of quantum logic gates and (simultaneously) the associated state preparation and measurement (SPAM) operations.  GST is self-calibrating.  This eliminates a key limitation of traditional quantum state and process tomography, which characterize either states (assuming perfect processes) or processes (assuming perfect state preparation and measurement), but not both together.  Compared with benchmarking protocols such as randomized benchmarking, GST provides much more detailed and accurate information about the gates, but demands more data.  The primary downside of GST has been its complexity.  Whereas benchmarking and state/process tomography data can be analyzed with relatively simple algorithms, GST requires more complex algorithms and more fine-tuning (linear GST is an exception that can be implemented easily).  pyGSTi addresses and eliminates this obstacle by providing a fully-featured, publicly available implementation of GST in the Python programming language.

The primary goals of the pyGSTi project are to:

- provide efficient and robust implementations of Gate Set Tomography algorithms;
- allow straightforward interoperability with other software;
- provide a powerful high-level interface suited to inexperienced programmers, so that
  common GST tasks can be performed using just one or two lines of code;
- use modular design to make it easy for users to modify, customize, and extend GST functionality.


