# pkcrypt2

Help on module pkcrypt2:

## NAME
  pkcrypt2 - Public key encryption utility library, simplified.
  Mostly tested with python2.7

## DESCRIPTION
  - Examples:
    
    Here are most likely the most common things you want to do
    with this library:

        pkcrypt2.py -g >g # generate a key

        pkcrypt2.py --ykey g -sign     --yenv<makefile | tee makefile.sig # sign a document

        pkcrypt2.py --ykey g -sign2    --yenv<makefile | tee makefile.sig2 # signature + original file

        pkcrypt2.py --ykey g -sign  -r --yenv<makefile # same as above but ripemd160 added on start
        pkcrypt2.py --ykey g -sign2 -r --yenv<makefile

        pkcrypt2.py --ykey g -verify   --yenv<makefile.sig2 # verify aforementioned makefile against g

        pkcrypt2.py          -verify2  --yenv<makefile.sig2 # verify aforementioned makefile

        pkcrypt2.py -mine makefile.sig2 --skip # this will mine for a RIPEMD160 starting with --prefix
	
## CLASSES
    __builtin__.object
        BaseEnvelope
            Envelope(BaseEnvelope, SaveLoadFileMixin, RipeMD160HashMixin)
                YamlEnvelope
        BaseKey
            Key(BaseKey, SaveLoadFileMixin, RipeMD160HashMixin)
                YamlKey
    RipeMD160HashMixin
    SaveLoadFileMixin
    
    class BaseEnvelope(__builtin__.object)
     |  Methods defined here:
     |  
     |  __init__(_, msg, prefix='', suffix='')
     |  
     |  __repr__(_)
     |  
     |  __str__(_)
     |  
     |  sign(_, secret)
     |  
     |  verify(_, secret)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  thaw(_, str) from __builtin__.type
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  freeze
     |  
     |  full_msg
     |  
     |  sig_line
    
    class BaseKey(__builtin__.object)
     |  Methods defined here:
     |  
     |  __init__(_, vkey='', skey='')
     |  
     |  __repr__(_)
     |  
     |  __str__(_)
     |  
     |  sign(_, msg)
     |  
     |  verify(_, msg, sig, raise_error=True)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  thaw(_, s) from __builtin__.type
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  freeze
     |  
     |  keys
     |  
     |  public
     |  
     |  secret
     |  
     |  short
    
    class Envelope(BaseEnvelope, SaveLoadFileMixin, RipeMD160HashMixin)
     |  Method resolution order:
     |      Envelope
     |      BaseEnvelope
     |      __builtin__.object
     |      SaveLoadFileMixin
     |      RipeMD160HashMixin
     |  
     |  Methods inherited from BaseEnvelope:
     |  
     |  __init__(_, msg, prefix='', suffix='')
     |  
     |  __repr__(_)
     |  
     |  __str__(_)
     |  
     |  sign(_, secret)
     |  
     |  verify(_, secret)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from BaseEnvelope:
     |  
     |  thaw(_, str) from __builtin__.type
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseEnvelope:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  freeze
     |  
     |  full_msg
     |  
     |  sig_line
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from SaveLoadFileMixin:
     |  
     |  save_fname(_, filename)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from SaveLoadFileMixin:
     |  
     |  load_fname(_, filename) from __builtin__.type
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from RipeMD160HashMixin:
     |  
     |  __eq__(_, other)
     |  
     |  __gt__(_, other)
     |  
     |  __lt__(_, other)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from RipeMD160HashMixin:
     |  
     |  hash
     |  
     |  hexdigest
    
    class Key(BaseKey, SaveLoadFileMixin, RipeMD160HashMixin)
     |  Method resolution order:
     |      Key
     |      BaseKey
     |      __builtin__.object
     |      SaveLoadFileMixin
     |      RipeMD160HashMixin
     |  
     |  Methods inherited from BaseKey:
     |  
     |  __init__(_, vkey='', skey='')
     |  
     |  __repr__(_)
     |  
     |  __str__(_)
     |  
     |  sign(_, msg)
     |  
     |  verify(_, msg, sig, raise_error=True)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from BaseKey:
     |  
     |  thaw(_, s) from __builtin__.type
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseKey:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  freeze
     |  
     |  keys
     |  
     |  public
     |  
     |  secret
     |  
     |  short
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from SaveLoadFileMixin:
     |  
     |  save_fname(_, filename)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from SaveLoadFileMixin:
     |  
     |  load_fname(_, filename) from __builtin__.type
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from RipeMD160HashMixin:
     |  
     |  __eq__(_, other)
     |  
     |  __gt__(_, other)
     |  
     |  __lt__(_, other)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from RipeMD160HashMixin:
     |  
     |  hash
     |  
     |  hexdigest
    
    class RipeMD160HashMixin
     |  Methods defined here:
     |  
     |  __eq__(_, other)
     |  
     |  __gt__(_, other)
     |  
     |  __hash__(_)
     |  
     |  __lt__(_, other)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  hash
     |  
     |  hexdigest
    
    class SaveLoadFileMixin
     |  Methods defined here:
     |  
     |  save_fname(_, filename)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  load_fname(_, filename) from __builtin__.classobj
    
    class YamlEnvelope(Envelope)
     |  Method resolution order:
     |      YamlEnvelope
     |      Envelope
     |      BaseEnvelope
     |      __builtin__.object
     |      SaveLoadFileMixin
     |      RipeMD160HashMixin
     |  
     |  Methods defined here:
     |  
     |  __init__(_, msg, *a, **kw)
     |  
     |  sign(_, secret)
     |  
     |  verify(_, k=None)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  mk_date_line(_) from __builtin__.type
     |  
     |  thaw(_, str) from __builtin__.type
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  sig_line
     |  
     |  verify_line
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseEnvelope:
     |  
     |  __repr__(_)
     |  
     |  __str__(_)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseEnvelope:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  freeze
     |  
     |  full_msg
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from SaveLoadFileMixin:
     |  
     |  save_fname(_, filename)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from SaveLoadFileMixin:
     |  
     |  load_fname(_, filename) from __builtin__.type
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from RipeMD160HashMixin:
     |  
     |  __eq__(_, other)
     |  
     |  __gt__(_, other)
     |  
     |  __lt__(_, other)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from RipeMD160HashMixin:
     |  
     |  hash
     |  
     |  hexdigest
    
    class YamlKey(Key)
     |  Method resolution order:
     |      YamlKey
     |      Key
     |      BaseKey
     |      __builtin__.object
     |      SaveLoadFileMixin
     |      RipeMD160HashMixin
     |  
     |  Class methods defined here:
     |  
     |  thaw(_, str) from __builtin__.type
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  freeze
     |  
     |  full_msg
     |  
     |  yaml_public
     |  
     |  yaml_secret
     |  
     |  yaml_sig
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseKey:
     |  
     |  __init__(_, vkey='', skey='')
     |  
     |  __repr__(_)
     |  
     |  __str__(_)
     |  
     |  sign(_, msg)
     |  
     |  verify(_, msg, sig, raise_error=True)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseKey:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  keys
     |  
     |  public
     |  
     |  secret
     |  
     |  short
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from SaveLoadFileMixin:
     |  
     |  save_fname(_, filename)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from SaveLoadFileMixin:
     |  
     |  load_fname(_, filename) from __builtin__.type
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from RipeMD160HashMixin:
     |  
     |  __eq__(_, other)
     |  
     |  __gt__(_, other)
     |  
     |  __lt__(_, other)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from RipeMD160HashMixin:
     |  
     |  hash
     |  
     |  hexdigest

## FUNCTIONS
    long_decode(s)
    
    long_encode(n)
    
    main()
    
    mine_file(filename, prefix='f00f', skip_line=True)
    
    sig2str(rs)
    
    sk2str(sk)
    
    str2sig(st)
    
    str2sk(st)
    
    str2vk(st)
    
    vk2str(vk)

## DATA
    __version__ = '1.1.0'

## VERSION
    1.1.0


