import os

home = os.environ["HOME"]

#os.environ["PATH"] = "%s/local/bin:%s/local/node/npm/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin" % (home, home)
os.environ["PATH"] = "%s/local/bin:%s/.rvm/gems/ruby-2.0.0-p353/bin:%s/local/node/npm/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin" % (home, home, home)
os.environ["GEM_HOME"] = "%s/.rvm/gems/ruby-2.0.0-p353/" % (home)
os.environ["GEM_PATH"] = os.environ["GEM_HOME"]

print ("PATH=%s" % os.environ["PATH"])
print ("GEM_HOME=%s" % os.environ["GEM_HOME"])
print ("GEM_PATH=%s" % os.environ["GEM_PATH"])
